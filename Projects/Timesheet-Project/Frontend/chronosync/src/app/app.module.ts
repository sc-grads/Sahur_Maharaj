import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {AdminPannelComponent} from "./components/admin-pannel/admin-pannel.component";


@NgModule({
  declarations: [
    AppComponent,
    AdminPannelComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
