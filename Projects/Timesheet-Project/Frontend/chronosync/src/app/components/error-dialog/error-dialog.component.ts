import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-error-dialog',
  templateUrl: './error-dialog.component.html',
  styleUrls: ['./error-dialog.component.css']
})
export class ErrorDialogComponent implements OnInit {
  @Input() message: string = '';
  show: boolean = true;

  constructor() { }

  ngOnInit(): void {
    // Hide the message after 2 seconds
    setTimeout(() => {
      this.show = false;
    }, 1500);
  }

  close(): void {
    this.show = false;
  }

}
