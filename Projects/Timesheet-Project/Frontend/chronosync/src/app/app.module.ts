import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
<<<<<<< HEAD

@NgModule({
  declarations: [
    AppComponent
=======
import { AddemployeeComponent } from './components/addemployee/addemployee.component';

@NgModule({
  declarations: [
    AppComponent,
    AddemployeeComponent
>>>>>>> 6a54678b6e4917cffaca909a201ab0919a9156bc
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
