import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CalcTimeService {

  constructor() { }

  calculateSpentTime(startTime:string, endTime:string, spentTime:string) {
    if (startTime && endTime) {
      const startAmPm = this.getAmPm(startTime);
      const endAmPm = this.getAmPm(endTime);

      const startTime24 = this.convertTo24HourFormat(startTime);
      const endTime24 = this.convertTo24HourFormat(endTime);

      const start = new Date(`2000-01-01T${startTime24}`);
      const end = new Date(`2000-01-01T${endTime24}`);

      if (startAmPm === 'PM' && endAmPm === 'AM') {
        end.setDate(end.getDate() + 1); // Add 1 day if end time is in the next day
      }

      const diffInMs = end.getTime() - start.getTime();
      if (diffInMs >= 0) {
        const hours = Math.floor(diffInMs / (1000 * 60 * 60));
        const minutes = Math.floor((diffInMs % (1000 * 60 * 60)) / (1000 * 60));
        spentTime = `${this.padZero(hours)}H${this.padZero(minutes)}`;
      } else {
        spentTime = 'Invalid Time'; // Display an error message for negative time
      }
    } else {
      spentTime = 'Invalid Time';
    }
    return spentTime;
  }

  padZero(value: number): string {
    return value.toString().padStart(2, '0');
  }

  getAmPm(time: string): string {
    const [hours, minutes] = time.split(':');
    const parsedHours = parseInt(hours, 10);

    return parsedHours >= 12 ? 'PM' : 'AM';
  }

  convertTo24HourFormat(time: string): string {
    const [hours, minutes, amPm] = time.split(':');
    const parsedHours = parseInt(hours, 10);

    // Check if the time is already in 24-hour format
    if (amPm === undefined && parsedHours < 24) {
      return time; // Return the original time if it's already in 24-hour format
    }

    if (amPm === 'PM' && parsedHours < 12) {
      return `${parsedHours + 12}:${minutes}`;
    } else if (amPm === 'AM' && parsedHours === 12) {
      return `00:${minutes}`;
    } else {
      return `${hours}:${minutes}`;
    }
  }
}
