import { Injectable } from '@angular/core';
import {DataModel} from "../models/data.model";


@Injectable({
  providedIn: 'root'
})
export class DataService {
  private _data: DataModel | undefined;
  clients: DataModel[] = [];

  constructor() { }

  setClient(data: DataModel) {
    this._data = data;
  }

  getClient(): DataModel {
    return <DataModel>this._data;
  }

   setClients(clients: DataModel[]): void {
    this.clients = clients;
  }

  getClients(): DataModel[] {
    return this.clients;
  }
}
