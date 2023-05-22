import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import {ServerInterface} from "../../interfaces/server-interface";
import {EncryptorService} from "../backend/encryptor.service";

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private apiURL:string = 'http://localhost:5000/endpoint/login';
  constructor(private httpC: HttpClient, private encapsvc:EncryptorService) { }

  postInfo(userName:string, password:string){
    let loginData = {'User': userName, 'Password': this.encapsvc.encryptPassword(password,userName)};
    return this.httpC.post<ServerInterface>(this.apiURL, loginData);
  }
}
