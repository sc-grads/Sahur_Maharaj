import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {LoginComponent} from "../components/login/login.component";

interface userData{
  userid: number;
  clientid: number;
  taskid: number;
  timesheetid: number;
  totalid: number;
}

interface userResponse{
  status: string;
  message?: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private httpClient: HttpClient, private loggedin: LoginComponent) { }
  private userendpoint = `http://localhost:5000/endpoint/${this.loggedin.username}`;

  getData(userid: number, clientid:number, taskid:number, timesheetid:number, totalid:number){
    const data: userData = {userid: userid, clientid:clientid, taskid:taskid, timesheetid:timesheetid, totalid:totalid};
    return this.httpClient.post<userResponse>(`${this.userendpoint}`, data);
  }

}
