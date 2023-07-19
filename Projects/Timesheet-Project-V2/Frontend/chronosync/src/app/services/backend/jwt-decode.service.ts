import { Injectable } from '@angular/core';
import jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class JwtDecodeService {
  constructor() { }

  decryptToken(token: string): any {
    try {
      return jwt_decode<any>(token);
    } catch (error) {
      console.error('Error while decrypting JWT:', error);
      return null;
    }
  }
}
