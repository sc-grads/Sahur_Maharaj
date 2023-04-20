import { Component } from '@angular/core';
import { LoginService } from "../../services/login.service";
import { Router } from "@angular/router";
import {User} from '../../models/user.model'
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  // html variables
  email:string = '';
  password:string='';

  constructor(
    private validateService: LoginService,
    private router: Router,
    private userService: UserService
  ) { }

  // send data to service for login
  login() {
    this.validateService.send(this.email, this.password).subscribe((r: any) => {
      if (r.message == 'OK') {
        const user = new User(
          r.Data.id,
          r.Data.fname,
          r.Data.lname,
          r.Data.email,
          r.Data.hash,
          r.Data.type
        );
        this.userService.setUser(user);
        this.router.navigate(['/user', user.firstName]).then(r => console.log(`navigated: ${r}`));
      }else {
        alert(r.message);
      }
    });
  }
}
