import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import {EncryptorService} from "../backend/encryptor.service";

interface Login{
  username:string;
  password:string;
  usertype:string;
  message:string;
  token?:string;
}

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private apiURL:string = 'http://localhost:5000/endpoint/login';
  constructor(private httpC: HttpClient, private encapsvc:EncryptorService) { }

  postInfo(userName:string, password:string){
    let loginData = {'User': userName, 'Password': this.encapsvc.encryptPassword(password,userName)};
    //console.log(this.encapsvc.encryptPassword(password,userName))
    return this.httpC.post<Login>(this.apiURL, loginData);
  }
}
