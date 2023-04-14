import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

interface UserData {
  userid: number;
  clientid: number;
  taskid: number;
  timesheetid: number;
  totalid: number;
}

interface UserResponse {
  status: string;
  message?: string;
}

@Injectable({
  providedIn: 'root'
})
export class UserService {

  private userendpoint: string = '';

  constructor(private httpClient: HttpClient) { }

  getData(userid: number, clientid: number, taskid: number, timesheetid: number, totalid: number, submit: string) {
    this.userendpoint = `http://localhost:5000/endpoint/login/${submit}`;
    const data: UserData = { userid, clientid, taskid, timesheetid, totalid };
    return this.httpClient.post<UserResponse>(`${this.userendpoint}`, data);
  }
}
