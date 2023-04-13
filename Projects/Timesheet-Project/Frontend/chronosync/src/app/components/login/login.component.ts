import { Component } from '@angular/core';
import { LoginService } from "../../services/login.service";
import * as CryptoJS from 'crypto-js';
import { Router } from '@angular/router'


interface LoginResponse {
  status: string;
  message?: string;
  access_level?:string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username: string = '';
  password: string = '';
  errorMessage: string | undefined = '';

  constructor(private loginsrv: LoginService, private router: Router) {  }

 submit() {
  this.errorMessage = ''; // reset error message
  const hashedPassword = CryptoJS.SHA256(this.password).toString();
  this.loginsrv.login(this.username, hashedPassword).subscribe((response: LoginResponse) => {
    if (response.status === 'success') {
      console.log('Login successful!');
      console.log('Access Level: ' + response.access_level);
      if (response.access_level === 'SUPERUSER') {
        this.router.navigate(['/admin']).then(r => console.log('Admin Access'));
      } else {
        this.router.navigate(['/user']).then(r => console.log('User Access'));
      }
    } else {
      console.log('Login failed: ' + response.message);
      this.errorMessage = response.message;
    }
  });
}

}
