import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {

  employeeTypes = ['standard', 'superuser'];
  selectedEmployeeType = this.employeeTypes[0];

}
