import { Component } from '@angular/core';
import { LoginService } from '../../services/api/login.service';
import {JwtDecodeService} from "../../services/backend/jwt-decode.service";
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  email: string = '';
  password: string = '';
  message: string = '';

  constructor(private logSrv: LoginService, private router: Router, private decode: JwtDecodeService) { }

  login() {
    this.logSrv.postInfo(this.email, this.password).pipe(
      catchError((error) => {
        console.error(error);
        this.message = 'Incorrect Email or Password: ' + error.status; // Set a default error message
        return throwError(error);
      })
    ).subscribe((response) => {
      this.message = response.message;
      const token = response.token || '';
      const decodedToken = this.decode.decryptToken(token);

      console.log(decodedToken.usertype);
      if (decodedToken.usertype === 'STANDARD') {
        this.router.navigate(['stdUser', token]).then((r) => console.log(r));
      }
      else if (decodedToken.usertype === 'SUPERUSER'){
        this.router.navigate(['sprUser', token]).then((r) => console.log(r));
      }
    });
  }
}
