import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

// interface
interface timesheetData{
  date:string;
  billable:string;
  clientid:number;
  taskid:number;
  project:string;
  comment:string;
  timeS:string;
  timeE:string;
  timeT:string;
}
@Injectable({
  providedIn: 'root'
})
export class InsertTimeEntryService {

  private inserturl:string = 'http://localhost:5000/endpoint/insert';

  constructor(private httpC:HttpClient) { }
  send(date:string,
       billable:string,
       clientid:number,
       taskid:number,
       project:string,
       comment:string,
       timeS:string,
       timeE:string,
       timeT:string){
    let timeData = {'cdate':date, 'billable':billable, 'clientid':clientid,
    'taskid':taskid, 'project':project, 'comment':comment, 'starttime':timeS, 'endtime':timeE, 'totaltime':timeT};
    return this.httpC.post<timesheetData>(this.inserturl, timeData);

  }
}
