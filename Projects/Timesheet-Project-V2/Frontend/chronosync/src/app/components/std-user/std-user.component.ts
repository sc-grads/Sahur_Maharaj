import { Component, OnInit } from '@angular/core';
import {DataloadService} from "../../services/api/dataload.service";
@Component({
  selector: 'app-std-user',
  templateUrl: './std-user.component.html',
  styleUrls: ['./std-user.component.css']
})
export class StdUserComponent {
  user:string = '';

  constructor(private  dls:DataloadService) { }

  ngOnInit(){
    this.dls.loadData().subscribe((response) =>{
          this.user = response.userName;
    });
  }

}
