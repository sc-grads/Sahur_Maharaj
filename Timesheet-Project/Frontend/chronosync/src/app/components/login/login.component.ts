import { Component } from '@angular/core';
import {LoginserviceService} from "../../services/loginservice/loginservice.service";
import {Router} from "@angular/router";
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  constructor(private login: LoginserviceService, private router: Router) { }

  user_name:string = '';
  user_password:string = '';
  user_id: number = 0;
  async onLogin() {
    await this.login.login(this.user_name, this.user_password).subscribe(response => {
      if(response != 404){
        console.debug('Login Success');
        alert(`Login Success for user: ${this.user_name}`);
        alert(response)
        this.router.navigate(['/user', this.user_id]);
      }else {
        console.debug(response);
        alert('User name or password is incorrect.');
        this.user_name = '';
        this.user_password = '';
        this.router.navigate(['/404']).then(r => {console.debug('redirect')});
      }

    });

  }
}
