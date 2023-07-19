import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface LoadData {
  userid: number;
  userName:string;
  clients: any[];
  tasks: any[];
  timesheet: any[];
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataloadService {

  private apiURL: string = 'http://localhost:5000/endpoint/load';

  constructor(private httpClient: HttpClient) { }

  loadData() {
    return this.httpClient.get<LoadData>(this.apiURL);
  }
}
