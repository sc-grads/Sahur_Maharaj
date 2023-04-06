import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { RegEmployeeComponent } from './components/reg-employee/reg-employee.component';

@NgModule({
  declarations: [
    AppComponent,
    RegEmployeeComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
