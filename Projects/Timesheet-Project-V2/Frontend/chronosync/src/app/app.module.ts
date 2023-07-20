import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import {FormsModule} from "@angular/forms";
import { HttpClientModule } from '@angular/common/http';
import { StdUserComponent } from './components/std-user/std-user.component';
import { SprUserComponent } from './components/spr-user/spr-user.component';
import { ClockTimeComponent } from './components/clock-time/clock-time.component';
import { TimesheetComponent } from './components/timesheet/timesheet.component';
import { DatePipe } from '@angular/common';


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    StdUserComponent,
    SprUserComponent,
    ClockTimeComponent,
    TimesheetComponent,

  ],
    imports: [
        BrowserModule,
        AppRoutingModule,
        FormsModule,
        HttpClientModule
    ],
  providers: [DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
