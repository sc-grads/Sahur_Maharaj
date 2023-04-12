import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {AdminPanelComponent} from "./components/admin-panel/admin-panel.component";
import { UserPannelComponent } from './components/user-pannel/user-pannel.component';
import { UserAnalyticPannelComponent } from './components/user-analytic-pannel/user-analytic-pannel.component';
import { AdminAnalyticPannelComponent } from './components/admin-analytic-pannel/admin-analytic-pannel.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';


@NgModule({
  declarations: [
    AppComponent,
    AdminPanelComponent,
    UserPannelComponent,
    UserAnalyticPannelComponent,
    AdminAnalyticPannelComponent,
    LoginComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
