import { Component } from '@angular/core';
import { RegistrationService } from '../../services/registration.service';

@Component({
  selector: 'app-reg-employee',
  templateUrl: './reg-employee.component.html',
  styleUrls: ['./reg-employee.component.css']
})
export class RegEmployeeComponent {
  // variables
  firstName: string = '';
  lastName: string = '';
  emailAddr: string = '';
  password: string = '';
  confirmPassword: string = '';
  employeeType: string[] = ['Guest', 'User', 'Admin'];
  selectedType: string = '';
  isButtonDisabled: boolean = true;
  errorMessage: string = '';

  // constructor
  constructor(private regService: RegistrationService) {}

  onSubmit() {
    // Check if all required fields are filled
    if (!this.firstName.trim() || !this.lastName.trim() || !this.emailAddr.trim() || !this.password.trim() || !this.selectedType) {
      this.errorMessage = 'Please fill out all required fields!';
      this.isButtonDisabled = true;
      return;
    }

    this.isButtonDisabled = false;
    this.errorMessage = '';
  }

  async submit() {
    try {
      await this.regService.sendUserInfo(
        this.firstName.trim(),
        this.lastName.trim(),
        this.emailAddr.trim(),
        this.password.trim(),
        this.selectedType
      ).subscribe();
    } catch (error) {
      console.error('Error:', error);
    }
  }
}
