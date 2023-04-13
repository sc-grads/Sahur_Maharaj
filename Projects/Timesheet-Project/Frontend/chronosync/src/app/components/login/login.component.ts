import { Component } from '@angular/core';
import { LoginService } from "../../services/login.service";
import * as bcrypt from "bcryptjs";

interface LoginResponse {
  status: string;
  message?: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';

  constructor(private loginsrv: LoginService) {  }

  submit(){
    const hashedPassword = bcrypt.hashSync(this.password, 10);
    this.loginsrv.login(this.username, hashedPassword).subscribe((response: LoginResponse) => {
      if (response.status === 'success') {
        console.log('Login successful!');
      } else {
        console.log('Login failed: ' + response.message);
      }
    });
  }
}
