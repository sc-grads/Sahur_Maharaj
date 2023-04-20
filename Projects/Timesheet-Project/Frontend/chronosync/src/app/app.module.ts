import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import {FormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import { Routes, RouterModule } from '@angular/router';
import { UserPanelComponent } from './components/user-panel/user-panel.component';

const routes: Routes = [
  {path: '', component: LoginComponent},
  {path: 'user/:user', component: UserPanelComponent},


];

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    UserPanelComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
