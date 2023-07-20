import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

interface timeClock{
  userid:number;
  date:string;
  billable:string;
  project:string;
  client:string;
  task:string;
  comment:string;
  startTime:string;
  endTime:string;
  spentTime:string;
}
@Injectable({
  providedIn: 'root'
})
export class ClocktimeService {
  private apiURL:string = 'http://localhost:5000/endpoint/clockentry';

  constructor(private clockTClient: HttpClient) { }
  subClockData(clockData:timeClock){
    return this.clockTClient.post<timeClock>(this.apiURL, clockData);
  }

}
