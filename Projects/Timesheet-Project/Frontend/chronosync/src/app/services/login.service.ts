import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AuthService} from "./auth.service";

// user interface for service
interface userPostData{
  email:string;
  password:string;
}

@Injectable({
  providedIn: 'root'
})

export class LoginService {

  // login url for api
  private loginendpoint: string = 'http://localhost:5000/endpoint/login'

  constructor(private httpC: HttpClient, private auth:AuthService) { }
  send(email:string, password: string){
    // encrypt password
    let hash = this.auth.encryptPassword(password, email)
    let userData = {'email': email, 'password': hash};
    return this.httpC.post<userPostData>(this.loginendpoint, userData);

  }

}
