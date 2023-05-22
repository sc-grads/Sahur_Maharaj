import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {ServerInterface} from "../../interfaces/server-interface";
@Injectable({
  providedIn: 'root'
})
export class DataloadService {

  constructor(private httpC: HttpClient) { }
  private apiURL:string = 'http://localhost:5000/endpoint/load'
  loadData(){
    return this.httpC.get<ServerInterface>(this.apiURL);
  }


}
