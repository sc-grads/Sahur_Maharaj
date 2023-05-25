import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import {ServerInterface} from "../../interfaces/server-interface";
@Injectable({
  providedIn: 'root'
})
export class ClockentryService {

  private apiURL:string = 'http://localhost:5000/endpoint/clockentry';
  constructor(private http: HttpClient) {}

  submitData(clockData: any) {
    return this.http.post<ServerInterface>(this.apiURL, clockData);
  }
}
