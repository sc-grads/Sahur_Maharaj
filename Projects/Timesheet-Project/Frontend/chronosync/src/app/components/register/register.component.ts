import { Component } from '@angular/core';
import {RegisterService} from "../../services/register.service";
import * as CryptoJS from 'crypto-js';

interface RegisterResponse {
  status: string;
  message?: string;
}
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  firstName:string = '';
  lastName:string = '';
  email:string = '';
  password:string = '';
  employeeTypes = ['STANDARD', 'SUPERUSER'];
  selectedEmployeeType = this.employeeTypes[0];
  errorMessage: string | undefined = '';

  constructor(private regSvc: RegisterService) {  }

  register(){
    this.errorMessage = ''; // reset error message
    const hashedPassword = CryptoJS.SHA256(this.password).toString();
    this.regSvc.register(this.firstName, this.lastName, this.email, hashedPassword, this.selectedEmployeeType).subscribe
    ((response: RegisterResponse) => {
      if (response.status === 'success') {
        console.log('Registration successful!');
      } else {
        this.errorMessage = `User Already Exists`;
        console.log('Registration failed: ' + response.message);
      }
    });
  }


}
