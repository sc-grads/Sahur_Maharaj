import { Component, OnInit } from '@angular/core';
import { DataloadService } from "../../services/api/dataload.service";
import { ServerInterface } from "../../interfaces/server-interface";
import { ActivatedRoute } from '@angular/router';
import {ClockentryService} from "../../services/api/clockentry.service";

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
  comment:string = '';

constructor(private dlc: DataloadService, private route: ActivatedRoute, private clockService: ClockentryService) {}
    isFormValid(): "" | false | string {
    return this.date && this.billable !== undefined && this.project && this.selectedClient && this.selectedTask && this.startTime && this.endTime;
  }

  ngOnInit(): void {
    this.userId = this.route.snapshot.params['userid'];
    this.date = new Date().toISOString().split('T')[0];

    this.dlc.loadData(this.userId).subscribe(
      (response: ServerInterface) => {
        console.log(response);
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
      },
      (error) => {
        console.error(error);
        this.message = 'Failed to load data: ' + error.status;
      }
    );
  }



  addConcatenatedOption() {
    const concatenatedClient = this.clients
      .map(client => `${client.Name} - ${client.Description}`)
      .join(', ');

    this.clients.unshift({ Name: 'All Clients', Description: concatenatedClient });
  }

  addConcatenatedOptionForTasks() {
    const concatenatedTask = this.tasks
      .map(task => `${task.Name} - ${task.Description}`)
      .join(', ');

    this.tasks.unshift({ Name: 'All Tasks', Description: concatenatedTask });
  }

  calculateSpentTime() {
    if (this.startTime && this.endTime) {
      const start = new Date(`2000-01-01T${this.startTime}`);
      const end = new Date(`2000-01-01T${this.endTime}`);
      const diffInMs = end.getTime() - start.getTime();
      const hours = Math.floor(diffInMs / (1000 * 60 * 60));
      const minutes = Math.floor((diffInMs % (1000 * 60 * 60)) / (1000 * 60));
      this.spentTime = `${this.padZero(hours)}H${this.padZero(minutes)}`;
    } else {
      this.spentTime = '';
    }
  }

  padZero(value: number): string {
    return value.toString().padStart(2, '0');
  }

  submitClockData() {
  const clockData = {
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
  };

  this.clockService.submitData(clockData).subscribe(
    (response:any) => {
      console.log('Data submitted successfully:', response);
      // Reset the form or perform any necessary actions
    },
    (error:any) => {
      console.error('Failed to submit data:', error);
      // Handle the error accordingly
    }
  );
}

}
