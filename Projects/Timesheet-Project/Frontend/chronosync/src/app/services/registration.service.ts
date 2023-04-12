import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { SHA256, enc } from "crypto-js";

@Injectable({
  providedIn: 'root'
})
export class RegistrationService {
  // variables
  private readonly registerEndpoint: string = 'http://localhost:5000/endpoint/register';

  constructor(private httpClient: HttpClient) { }

  // send the user data to the flask back end
protected sendData(firstName: string, lastName: string, emailAddr: string, paswd: string, selectedType: string) {
    const salt = enc.Utf8.parse(SHA256(emailAddr).toString());
    const hashedPassword = SHA256(paswd + salt);
    const saltString = enc.Base64.stringify(salt);
    const hashedPasswordString = hashedPassword.toString();

    // convert user data to JSON string
    const userinfo = JSON.stringify({
      fname: firstName,
      lname: lastName,
      email: emailAddr,
      passwd: hashedPasswordString,
      salt: saltString,
      selectedT: selectedType
    });

    // Send the user info to the Flask backend
    return this.httpClient.post(this.registerEndpoint, userinfo, {
      headers: {'Content-Type': 'application/json'}
    });
}


  public sendUserInfo(firstName: string, lastName: string, emailAddr: string, paswd: string, selectedType: string) {
    return this.sendData(firstName, lastName, emailAddr, paswd, selectedType);
  }
}
