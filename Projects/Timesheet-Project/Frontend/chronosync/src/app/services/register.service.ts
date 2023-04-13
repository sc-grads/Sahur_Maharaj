import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
interface RegisterData {
  firstname:string;
  lastname:string;
  wemail: string;
  password: string;
  etype:string;
}

interface RegisterResponse {
  status: string;
  message?: string;
}
@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  constructor(private httpClient: HttpClient) { }
  private registerendpoint = 'http://localhost:5000/endpoint/register';

  register(firstName:string, lastName:string, wEmail:string, password:string, etype:string){
    const data: RegisterData = {firstname: firstName, lastname: lastName, wemail: wEmail, password: password, etype:etype};
    return this.httpClient.post<RegisterResponse>(this.registerendpoint, data);
  }

}
