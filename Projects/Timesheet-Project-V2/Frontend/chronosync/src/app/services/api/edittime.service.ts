import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

interface editedTime{
  userid:number;
  edate:string;
  ebillable:string;
  eproject:string;
  eclient:string;
  etask:string;
  ecomment:string;
  estartTime:string;
  eendTime:string;
  espentTime:string;
}
@Injectable({
  providedIn: 'root'
})
export class EdittimeService {

  apiURL:string = 'http://localhost:5000/endpoint/editsheetentry';
  constructor(private editClient:HttpClient) { }

  submitForUpdate(editData:editedTime){
    return this.editClient.post<editedTime>(this.apiURL, editData);
  }
}
