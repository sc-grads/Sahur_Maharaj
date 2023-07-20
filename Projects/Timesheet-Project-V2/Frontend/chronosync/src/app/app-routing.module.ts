import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {LoginComponent} from "./components/login/login.component";
import {StdUserComponent} from "./components/std-user/std-user.component";
import {SprUserComponent} from "./components/spr-user/spr-user.component";

const routes: Routes = [
  {path:'', component:LoginComponent},
  {path:'stdUser/:token',component:StdUserComponent},
  {path: 'sprUser/:token', component:SprUserComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
