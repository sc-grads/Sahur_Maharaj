import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";

interface Data{
  id:number;
  name:string;
  description:string;
}


@Injectable({
  providedIn: 'root'
})
export class DataloaderService {

  private loadurl: string = 'http://localhost:5000/endpoint/load';
  constructor(private httpC: HttpClient) { }
  getData(){
    return this.httpC.get<Data>(this.loadurl);

  }

}
