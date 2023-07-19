import { Component, OnInit } from '@angular/core';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { DataloadService } from '../../services/api/dataload.service';
import { CalcTimeService } from "../../services/backend/calc-time.service";
import { EdittimeService } from "../../services/api/edittime.service";
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-timesheet',
  templateUrl: './timesheet.component.html',
  styleUrls: ['./timesheet.component.css']
})
export class TimesheetComponent implements OnInit {
  message: string = '';
  userid: number = 0;
  timesheetData: any[] = [];
  clientData: any[] = [];
  taskData: any[] = [];
  selectedTimesheet: any = {};
  isEditing: boolean = false;
  spentTime: string = '';
  filteredTimesheetData: any[] = [];
  filterType: string = '';
  currentDay: string = '';

  constructor(
    private dls: DataloadService,
    private calcTimeService: CalcTimeService,
    private edts: EdittimeService,
    private datePipe: DatePipe
  ) { }

  ngOnInit() {
    this.dls.loadData().pipe(
      catchError((error: any) => {
        console.error(error);
        this.message = 'Failed to load data: ' + error.status;
        return throwError(error);
      })
    ).subscribe((response) => {
      this.userid = response.userid;
      this.timesheetData = response.timesheet;
      this.clientData = response.clients;
      this.taskData = response.tasks;
      this.populateClientAndTaskNames();
      this.timesheetData.reverse();
      this.filterByDay();
      this.getCurrentDay();
    });
  }

  formatDate(date: string | null): string {
    if (date !== null) {
      return this.datePipe.transform(new Date(date), 'EEEE - dd - MMMM - yyyy') || '';
    }
    return '';
  }

  populateClientAndTaskNames() {
    for (let timesheet of this.timesheetData) {
      let client = this.clientData.find((client) => client.id === timesheet.client_id);
      timesheet.client_name = client ? client.Name : '';

      let task = this.taskData.find((task) => task.id === timesheet.task_id);
      timesheet.task_name = task ? task.Name : '';
    }
  }

  calculateSpentTime() {
    const startTime = this.selectedTimesheet.start_time;
    const endTime = this.selectedTimesheet.end_time;
    this.spentTime = this.calcTimeService.calculateSpentTime(startTime, endTime, this.selectedTimesheet.spentTime);
  }

  openOverlay(timesheet: any) {
    this.selectedTimesheet = { ...timesheet };
    this.spentTime = '';
    this.isEditing = true;
  }

  saveChanges() {
    console.log('Edited Timesheet:', this.selectedTimesheet);
    this.edts.submitForUpdate(this.selectedTimesheet).pipe(
      catchError((error: any) => {
        console.error('Failed to save timesheet data:', error);
        return throwError(error);
      })
    ).subscribe((response) => {
      console.log('Timesheet data saved:', response);
      window.location.reload();
    });

    this.isEditing = false;
    this.selectedTimesheet = {};
  }

  closeOverlay() {
    this.isEditing = false;
    this.selectedTimesheet = null;
  }

  filterByYear() {
    this.filterType = 'year';
    const currentYear = new Date().getFullYear();
    this.filteredTimesheetData = this.timesheetData.filter((timesheet) => {
      const year = new Date(timesheet.date).getFullYear();
      return year === currentYear;
    });
  }

  filterByMonth() {
    this.filterType = 'month';
    const currentYear = new Date().getFullYear();
    const currentMonth = new Date().getMonth();
    const firstDayOfMonth = new Date(currentYear, currentMonth, 1);
    const lastDayOfMonth = new Date(currentYear, currentMonth + 1, 0);

    this.filteredTimesheetData = [];
    for (let day = lastDayOfMonth.getDate(); day >= firstDayOfMonth.getDate(); day--) {
      const date = new Date(currentYear, currentMonth, day).toDateString();
      const dayTimesheets = this.timesheetData.filter((timesheet) => {
        const timesheetDate = new Date(timesheet.date).toDateString();
        return timesheetDate === date;
      });

      if (dayTimesheets.length > 0) {
        this.filteredTimesheetData.push({
          date: date,
          timesheets: dayTimesheets
        });
      }
    }
  }

  filterByDay() {
    this.filterType = 'day';
    const daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

    this.filteredTimesheetData = [];

    for (let i = 0; i < 7; i++) {
      const currentDay = new Date();
      currentDay.setDate(currentDay.getDate() - (currentDay.getDay() - i + 6) % 7); // Adjust the calculation to start from Monday
      const date = currentDay.toDateString();
      const dayTimesheets = this.timesheetData.filter((timesheet) => {
        const timesheetDate = new Date(timesheet.date).toDateString();
        return timesheetDate === date;
      });

      this.filteredTimesheetData.push({
        dayOfWeek: daysOfWeek[i],
        timesheets: dayTimesheets
      });
    }
  }

  getCurrentDay() {
    const currentDate = new Date();
    const options: Intl.DateTimeFormatOptions = { weekday: 'long' };
    const formatter = new Intl.DateTimeFormat('en-US', options);
    this.currentDay = formatter.format(currentDate);
  }

  filterByClient(clientId: number) {
    this.filterType = 'client';
    this.filteredTimesheetData = this.timesheetData.filter((timesheet) => timesheet.client_id === clientId);
  }

  filterByTask(taskId: number) {
    this.filterType = 'task';
    this.filteredTimesheetData = this.timesheetData.filter((timesheet) => timesheet.task_id === taskId);
  }
}
