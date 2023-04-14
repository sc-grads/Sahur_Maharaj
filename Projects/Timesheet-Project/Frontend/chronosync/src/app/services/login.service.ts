import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

interface LoginData {
  username: string;
  password: string;
}

interface LoginResponse {
  status: string;
  message?: string;
}

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private loginEndpoint = 'http://localhost:5000/endpoint/login';

  constructor(private httpClient: HttpClient) { }

  login(email: string, password: string) {
    const username = email.split('.')[0];
    const data: LoginData = {username: email, password: password};
    return this.httpClient.post<LoginResponse>(`${this.loginEndpoint}`, data);
  }

}
