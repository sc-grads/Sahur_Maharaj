import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {RouterModule, Routes} from "@angular/router";
import { E404Component } from './components/e404/e404.component';
import { UserComponent } from './components/user/user.component';

const appRoutes: Routes = [
  {path: '', component: LoginComponent},
  {path: '404', component: E404Component},
];
@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    E404Component,
    UserComponent
  ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpClientModule,
        RouterModule.forRoot(appRoutes)
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
