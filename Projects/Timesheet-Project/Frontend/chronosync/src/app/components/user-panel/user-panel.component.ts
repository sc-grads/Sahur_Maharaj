import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { User } from '../../models/user.model';
import {DataModel} from "../../models/data.model";
import {DataService} from "../../services/data.service";
import {DataloaderService} from "../../services/dataloader.service";
import {InsertTimeEntryService} from '../../services/insert-time-entry.service';
@Component({
  selector: 'app-user-panel',
  templateUrl: './user-panel.component.html',
  styleUrls: ['./user-panel.component.css']
})

export class UserPanelComponent implements OnInit {
  // user model for cross data
  user: User | undefined;

  // variables
  cDate: string = '';
  billability:string[] = ['true', 'false'];
  billable:string = this.billability[0];
  clientlist:string[] = [];
  client:string = this.clientlist[0];
  tasklist: string[] = [];
  task:string = this.tasklist[0];
  // get id from the lists
  clientid: number = 0;
  taskid: number = 0;
  // strings
  projectname:string = '';
  comment:string = '';
  // time things
  timeS:string = '';
  timeE:string = '';
  timeT:string = '';

  constructor(private userService: UserService, private dls:DataloaderService, private dataService: DataService,
              private inserttimeentry: InsertTimeEntryService) {
    const today = new Date();
    this.cDate = today.toISOString().substring(0, 10);
  }

  // on load set user data
 ngOnInit() {
    // user object
  this.user = this.userService.getUser();
  // client object
  this.dls.getData().subscribe((r:any) => {
    if (r.clients && r.clients.length > 0) { // Check if response list is not empty
      const clients: DataModel[] = []; // Create empty list of clients
      for (const client of r.clients) { // Loop through clients in response list
        const newClient = new DataModel(client.id, client.name, client.description); // Create new client object
        clients.push(newClient); // Add new client object to list of clients
      }
      this.dataService.setClient(clients[0]); // Set first client as active client
      this.dataService.setClients(clients); // Set list of clients
      // add clients to global list to be displayed in html
      for (let i in this.dataService.getClients()) {
        let clientInf = `${this.dataService.getClients()[i].name} - ${this.dataService.getClients()[i].description}`;
        this.clientlist.push(clientInf);
      }
    }
  });
  // task object
   this.dls.getData().subscribe((r: any) => {
      if (r.tasks && r.tasks.length > 0) {
        const tasks: DataModel[] = [];
        for (const task of r.tasks) {
          const newTask = new DataModel(
            task.id,
            task.name,
            task.description
          );
          tasks.push(newTask);
        }
        this.dataService.setTasks(tasks);
        // add tasks to global list to be displayed in html
        for (const i in tasks) {
          let taskInf = `${tasks[i].name} - ${tasks[i].description}`;
          this.tasklist.push(taskInf);
        }
      }
    });

  }

  // update timeT when start or end time changes
updateTime() {
  if (this.timeS && this.timeE) { // Check that both time fields are not empty
    const start = new Date(`2000-01-01T${this.timeS}`);
    const end = new Date(`2000-01-01T${this.timeE}`);
    const diffMs = end.getTime() - start.getTime();
    const diffHrs = Math.floor((diffMs / (1000 * 60 * 60)) % 24);
    const diffMins = Math.floor((diffMs / (1000 * 60)) % 60);
    this.timeT = `${diffHrs < 10 ? '0' : ''}${diffHrs}H:${diffMins < 10 ? '0' : ''}${diffMins}M`;
  } else {
    this.timeT = ''; // Clear timeT field if either time field is empty
  }
}
// client_change
onClientChange(event: any) {
  const selectedIndex = event.target.selectedIndex;
  const selectedClient = this.dataService.getClients()[selectedIndex];
  this.clientid = selectedClient.id;
}

onTaskChange(event: any){
  const tIndex = event.target.selectedIndex;
  const sTask = this.dataService.getTasks()[tIndex];
  this.taskid = sTask.id;

}


// calculate time difference when start or end time changes
onStartTimeChange() {
  this.updateTime();
}

onEndTimeChange() {
  this.updateTime();
}


  // add an entry to the database
  addEntry(){
    console.log(this.clientid);
    console.log(this.taskid);
    this.inserttimeentry.send(this.cDate, this.billable, this.clientid,
        this.taskid, this.projectname, this.comment, this.timeS, this.timeE, this.timeT).subscribe((r:any) =>{
          console.log(r);
    });

    console.log(`date: ${this.cDate}\nbillable: ${this.billable}\nclient: ${this.client}\n
    task: ${this.task}\nproject: ${this.projectname}\ncomment: ${this.comment}\n startTime: ${this.timeS}
    \n endtime: ${this.timeE}\nTotalTime: ${this.timeT}`);

  }


}
