import { Injectable } from '@angular/core';
import * as sha256 from 'js-sha256';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  // return first val of email for salt
  private extractSalt(email: string): string {
    return email.split('@')[0];
  }

  // Function to hash the password using SHA256 algorithm and the salt
  private hashPassword(password: string, salt: string): string {
    return sha256.sha256(salt + password);
  }

  // Function to encrypt the password by generating a salt and then hashing the password with the salt
encryptPassword(password: string, email: string): string {
    const salt = this.extractSalt(email);
    const hash = this.hashPassword(password, salt);
    // spilt and salt
    let saltCharIndex = 0;
    let encryptedPassword = '';
    for (let i = 0; i < hash.length; i += 3) {
      encryptedPassword += hash.slice(i, i + 3);
      if (saltCharIndex < salt.length) {
        encryptedPassword += salt.charAt(saltCharIndex);
        saltCharIndex++;
      }
    }
    return encryptedPassword;
  }
  // Function to extract the salt from the encrypted password
  private extSalt(encryptedPassword: string): string {
    return encryptedPassword.slice(-32);
  }

}
