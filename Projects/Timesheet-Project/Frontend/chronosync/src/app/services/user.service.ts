import { Injectable } from '@angular/core';
import { User } from '../models/user.model'

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private _user: User | undefined;

  constructor() { }

  setUser(user: User) {
    this._user = user;
  }

  getUser(): User {
    return <User>this._user;
  }
}
