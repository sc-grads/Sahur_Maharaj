import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
@Injectable({
  providedIn: 'root'
})
export class LoginserviceService {
  constructor(private http: HttpClient) { }

  login(username:string,password:string){
    return this.http.post('http://localhost:5000/api/login',{username:username, password:password});
  }
}
