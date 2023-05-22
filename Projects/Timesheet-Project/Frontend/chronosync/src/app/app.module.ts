import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {RouterModule} from "@angular/router";
import { StandardUserComponent } from './components/standard-user/standard-user.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    StandardUserComponent
  ],
  imports: [
    RouterModule.forRoot([
      {path: '', component: LoginComponent},
      {path: 'standardUser/:userid', component: StandardUserComponent}
    ]),
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
