import { Component, OnInit } from '@angular/core';
import {DataloadService} from "../../services/api/dataload.service";
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import {CalcTimeService} from "../../services/backend/calc-time.service";
import {ClocktimeService} from "../../services/api/clocktime.service";

@Component({
  selector: 'app-clock-time',
  templateUrl: './clock-time.component.html',
  styleUrls: ['./clock-time.component.css']
})
export class ClockTimeComponent {
  userid: number = 0;
  date: string = '';
  billableOptions = [{ label: 'Yes', value: true },{ label: 'No', value: false }];
  billable: boolean = true;
  project: string = '';
  clients: any[] = [];
  selectedClient: string = 'None';
  tasks: any[] = [];
  selectedTask: string = 'None';
  startTime: string = '';
  endTime: string = '';
  spentTime: string = '';
  comment: string = '';
  message:string = '';

  constructor(private dls:DataloadService, private calcTime:CalcTimeService, private cTime:ClocktimeService) { }

  ngOnInit(){
    this.date = new Date().toISOString().split('T')[0];
    this.dls.loadData().pipe(
        catchError((error: any) => {
          console.error(error);
          this.message = 'Failed to load data: ' + error.status;
          return throwError(error);
        })
      ).subscribe((response) =>{
        // clients
      console.log(this.clients);
        this.clients = response.clients;
        if (this.clients.length > 0) {
          this.selectedClient = this.clients[0].Name;
        }
        this.addConcatenatedOption();
        // tasks
        this.tasks = response.tasks;
        if (this.tasks.length > 0) {
          this.selectedTask = this.tasks[0].Name;
        }
        this.addConcatenatedOptionForTasks();
        // set user id
      this.userid = response.userid;

    });
  }

    submitClockData(){
      const cData = {
      userid: this.userid,
      date: this.date,
      billable: this.billable.toString(),
      project: this.project,
      client: this.selectedClient,
      task: this.selectedTask,
      comment: this.comment,
      startTime: this.startTime,
      endTime: this.endTime,
      spentTime: this.spentTime
    };
    this.cTime.subClockData(cData).pipe(
      catchError((error: any) => {
          console.error('Failed to submit data:', error);
          return throwError(error);
        })
    ).subscribe((response) =>{
      console.log('Submitted');
      console.log(response)
      this.resetForm(); // reset form
      // reload page to display timesheet
      window.location.reload();
    });
    console.log('Click');
  }

  addConcatenatedOption() {
    const concatenatedClient = this.clients
      .map((client) => `${client.Name} - ${client.Description}`)
      .join(', ');

    this.clients.unshift({ Name: 'All Clients', Description: concatenatedClient });
  }

  addConcatenatedOptionForTasks() {
    const concatenatedTask = this.tasks
      .map((task) => `${task.Name} - ${task.Description}`)
      .join(', ');

    this.tasks.unshift({ Name: 'All Tasks', Description: concatenatedTask });
  }
  isFormValid():boolean{
    const isDateValid = !!this.date;
    const isBillableValid = this.billable !== undefined;
    const isProjectValid = !!this.project.trim();
    const isClientValid = !!this.selectedClient.trim();
    const isTaskValid = !!this.selectedTask.trim();
    const isStartTimeValid = !!this.startTime.trim();
    const isEndTimeValid = !!this.endTime.trim();
    const isTimeValid = this.isTimeValid(this.spentTime);
    return (
      isDateValid &&
      isBillableValid &&
      isProjectValid &&
      isClientValid &&
      isTaskValid &&
      isStartTimeValid &&
      isEndTimeValid &&
      isTimeValid
    );
  }

  resetForm() {
    this.billable = true;
    this.project = '';
    this.startTime = '';
    this.endTime = '';
    this.spentTime = '';
    this.comment = '';
  }
  isTimeValid(time: string): boolean {
  const timeRegex = /^(0[0-9]|1[0-2])H[0-5][0-9]$/;
  return timeRegex.test(time);
}
  calculateSpentTime(){
    this.spentTime = this.calcTime.calculateSpentTime(this.startTime, this.endTime, this.spentTime);
  }
  handleCommentChange(event:any){this.comment = event.target.value;}

  handleTaskChange(event:any){this.selectedTask = event.target.value;}

  handleClientChange(event:any){this.selectedClient = event.target.value;}

  handleProjectChange(event:any){this.project = event.target.value;}

  handleDateChange(event:any){this.date = event.target.value;}

}
