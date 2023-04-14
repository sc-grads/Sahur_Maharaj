import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {AdminPanelComponent} from "./components/admin-panel/admin-panel.component";
import { UserPannelComponent } from './components/user-pannel/user-pannel.component';
import { UserAnalyticPannelComponent } from './components/user-analytic-pannel/user-analytic-pannel.component';
import { AdminAnalyticPannelComponent } from './components/admin-analytic-pannel/admin-analytic-pannel.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { FormsModule } from "@angular/forms";

import { HttpClientModule } from "@angular/common/http";
import { RouterModule, Routes } from '@angular/router';
import { ErrorDialogComponent } from './components/error-dialog/error-dialog.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'user/:user', component: UserPannelComponent },
  { path: 'user_analytics/:user', component: UserAnalyticPannelComponent },
  { path: 'admin/:user', component: AdminPanelComponent },
  { path: 'admin_analytics/:user', component: AdminAnalyticPannelComponent },
  { path: '', redirectTo: '' }
];


@NgModule({
  declarations: [
    AppComponent,
    AdminPanelComponent,
    UserPannelComponent,
    UserAnalyticPannelComponent,
    AdminAnalyticPannelComponent,
    LoginComponent,
    RegisterComponent,
    ErrorDialogComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
