import { Component } from '@angular/core';
import {UserService} from "../../services/user.service";
@Component({
  selector: 'app-user-pannel',
  templateUrl: './user-pannel.component.html',
  styleUrls: ['./user-pannel.component.css']
})
export class UserPannelComponent {

  constructor(private usrsrv: UserService) {  }

  ngOnInit(){


  }



}
