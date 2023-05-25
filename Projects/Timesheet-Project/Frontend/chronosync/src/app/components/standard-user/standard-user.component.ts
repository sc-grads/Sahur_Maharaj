import { Component, OnInit } from '@angular/core';
import { DataloadService } from "../../services/api/dataload.service";
import { ServerInterface } from "../../interfaces/server-interface";
import { ActivatedRoute } from '@angular/router';
import { ClockentryService } from "../../services/api/clockentry.service";
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import {ReloadService} from "../../services/backend/reload.service";
@Component({
  selector: 'app-standard-user',
  templateUrl: './standard-user.component.html',
  styleUrls: ['./standard-user.component.css']
})

export class StandardUserComponent implements OnInit {
  message: string = '';
  userId: number = 0;
  date: string = '';
  billableOptions = [
    { label: 'Yes', value: true },
    { label: 'No', value: false }
  ];
  billable: boolean = true;
  project: string = '';
  clients: any[] = [];
  selectedClient: string = '';
  tasks: any[] = [];
  selectedTask: string = '';
  startTime: string = '';
  endTime: string = '';
  spentTime: string = '';
  comment: string = '';
  timesheetData: any[] = [];
  clientIds: number[] = [];
  taskIds:number[] = [];


  constructor(
    private dlc: DataloadService,
    private route: ActivatedRoute,
    private clockService: ClockentryService,
    private windowRef: ReloadService
  ) {}

  isFormValid(): boolean {
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

  isTimeValid(time: string): boolean {
  const timeRegex = /^(0[0-9]|1[0-2])H[0-5][0-9]$/;
  return timeRegex.test(time);
}

  ngOnInit(): void {
    this.userId = this.route.snapshot.params['userid'];
    this.date = new Date().toISOString().split('T')[0];

    this.dlc.loadData(this.userId)
      .pipe(
        catchError((error: any) => {
          console.error(error);
          this.message = 'Failed to load data: ' + error.status;
          return throwError(error);
        })
      )
      .subscribe((response: ServerInterface) => {
        console.log(response.data.clients[0].Name);

        this.clients = response.data.clients;
        if (this.clients.length > 0) {
          this.selectedClient = this.clients[0].Name;
        }
        this.addConcatenatedOption();

        this.tasks = response.data.tasks;
        if (this.tasks.length > 0) {
          this.selectedTask = this.tasks[0].Name;
        }
        this.addConcatenatedOptionForTasks();
        this.timesheetData = response.data.timesheet; // Assign the timesheet data directly
        // task names
        this.taskIds = this.timesheetData.map(timesheet => timesheet.task_id);
        for (const timesheet of this.timesheetData){
          const taskId = timesheet.task_id;
          const task = this.tasks.find(t => t.id === taskId);
          if (task){
            timesheet.task_name = task.Name;
          }
        }
        // client names
        this.clientIds = this.timesheetData.map(timesheet => timesheet.client_id);
        // Add client names based on client IDs
        for (const timesheet of this.timesheetData) {
          const clientId = timesheet.client_id;
          const client = this.clients.find(c => c.id === clientId);
          if (client) {
            timesheet.client_name = client.Name;
          }
        }


      });
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

  calculateSpentTime() {
    if (this.startTime && this.endTime) {
      const startAmPm = this.getAmPm(this.startTime);
      const endAmPm = this.getAmPm(this.endTime);

      const startTime24 = this.convertTo24HourFormat(this.startTime);
      const endTime24 = this.convertTo24HourFormat(this.endTime);

      const start = new Date(`2000-01-01T${startTime24}`);
      const end = new Date(`2000-01-01T${endTime24}`);

      if (startAmPm === 'PM' && endAmPm === 'AM') {
        end.setDate(end.getDate() + 1); // Add 1 day if end time is in the next day
      }

      const diffInMs = end.getTime() - start.getTime();
      if (diffInMs >= 0) {
        const hours = Math.floor(diffInMs / (1000 * 60 * 60));
        const minutes = Math.floor((diffInMs % (1000 * 60 * 60)) / (1000 * 60));
        this.spentTime = `${this.padZero(hours)}H${this.padZero(minutes)}`;
      } else {
        this.spentTime = 'Invalid Time'; // Display an error message for negative time
      }
    } else {
      this.spentTime = 'Invalid Time';
    }
  }

  padZero(value: number): string {
    return value.toString().padStart(2, '0');
  }

  getAmPm(time: string): string {
    const [hours, minutes] = time.split(':');
    const parsedHours = parseInt(hours, 10);

    return parsedHours >= 12 ? 'PM' : 'AM';
  }

  convertTo24HourFormat(time: string): string {
    const [hours, minutes, amPm] = time.split(':');
    const parsedHours = parseInt(hours, 10);

    if (amPm === 'PM' && parsedHours < 12) {
      return `${parsedHours + 12}:${minutes}`;
    } else if (amPm === 'AM' && parsedHours === 12) {
      return `00:${minutes}`;
    } else {
      return `${hours}:${minutes}`;
    }
  }

  handleDateChange(event: any) {
    this.date = event.target.value;
  }

  handleProjectChange(event: any) {
    this.project = event.target.value;
  }

  handleClientChange(event: any) {
    this.selectedClient = event.target.value;
  }

  handleTaskChange(event: any) {
    this.selectedTask = event.target.value;
  }

  handleCommentChange(event: any) {
    this.comment = event.target.value;
  }

  submitClockData() {
    const clockData: ServerInterface = {
      status: 200,
      message: 'Submitted Clock Data',
      data: {
        userId: this.userId,
        date: this.date,
        billable: this.billable,
        project: this.project,
        client: this.selectedClient,
        task: this.selectedTask,
        startTime: this.startTime,
        endTime: this.endTime,
        spentTime: this.spentTime,
        comment: this.comment
      }
    };

    this.clockService.submitData(clockData)
      .pipe(
        catchError((error: any) => {
          console.error('Failed to submit data:', error);
          return throwError(error);
        })
      )
      .subscribe((response: ServerInterface) => {
        console.log('Data submitted successfully:', response.message);
        this.windowRef.nativeWindow.location.reload();
        this.resetForm(); // Reset the form
      });
  }

  resetForm() {
    this.billable = true;
    this.project = '';
    this.startTime = '';
    this.endTime = '';
    this.spentTime = '';
    this.comment = '';
  }
}
