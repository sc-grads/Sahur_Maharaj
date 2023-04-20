import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { User } from '../../models/user.model';
import {DataModel} from "../../models/data.model";
import {DataService} from "../../services/data.service";
import {DataloaderService} from "../../services/dataloader.service";
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


  constructor(private userService: UserService, private dls:DataloaderService, private clientService: DataService) {
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
      this.clientService.setClient(clients[0]); // Set first client as active client
      this.clientService.setClients(clients); // Set list of clients
      // add clients to global list to be displayed in html
      for (const i in this.clientService.getClients()) {
        console.log(this.clientService.getClients()[i].name);
        this.clientlist.push(this.clientService.getClients()[i].name);
        console.log(this.clientService.getClients()[i].description);
      }
    }
  });
}


  // add an entry to the database
  addEntry(){
    console.log(this.clientlist);

  }


}
