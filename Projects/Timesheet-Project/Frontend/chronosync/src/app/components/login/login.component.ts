import { Component } from '@angular/core';
import { LoginService } from "../../services/api/login.service";
import { ServerInterface } from "../../interfaces/server-interface";
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { Router } from "@angular/router";

@Component({
  selector: 'app-loginInterface',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  message: string = '';

  constructor(private logSrv: LoginService, private redirect: Router) { }

  login() {
    this.logSrv.postInfo(this.email, this.password).pipe(
      catchError((error) => {
        console.error(error);
        this.message = 'Incorrect Email or Password: ' + error.status; // Set a default error message
        return throwError(error);
      })
    ).subscribe((response: ServerInterface) => {
      this.message = response.message;
      console.log(response.data.userStatus);
      if (response.data && response.data.userStatus === 'STANDARD') {
        this.redirect.navigate(['/standardUser']).then(r => console.log(r));
      }
    });
  }
}
