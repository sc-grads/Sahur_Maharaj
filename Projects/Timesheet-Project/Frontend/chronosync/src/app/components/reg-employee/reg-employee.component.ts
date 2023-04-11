import { Component } from '@angular/core';

@Component({
  selector: 'app-reg-employee',
  templateUrl: './reg-employee.component.html',
  styleUrls: ['./reg-employee.component.css']
})
export class RegEmployeeComponent {
  password: string | undefined;
  confirmPassword: string | undefined;

  submit() {
    if (this.password !== this.confirmPassword) {
      alert("Passwords don't match");
    } else {
      // submit the form
    }
  }

}
