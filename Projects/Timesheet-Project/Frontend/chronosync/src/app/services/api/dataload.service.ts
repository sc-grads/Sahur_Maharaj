import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { ServerInterface } from "../../interfaces/server-interface";

@Injectable({
  providedIn: 'root'
})
export class DataloadService {
  private apiURL: string = 'http://localhost:5000/endpoint/load';

  constructor(private http: HttpClient) {}

  loadData(userid:number) {
    return this.http.get<ServerInterface>(`${this.apiURL}userid=${userid}`);
  }
}
