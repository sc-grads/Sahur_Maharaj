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

  login(username: string, password: string) {
    const data: LoginData = {username: username, password: password};
    return this.httpClient.post<LoginResponse>(this.loginEndpoint, data);
  }

}
