export class TimeEntry {
  // variables
  private _id:number;
  private _t_date:string;
  private _t_billable:string;
  private _t_project:string;
  private _t_comment:string;
  private _t_start:string;
  private _t_end:string;
  private _t_spent:string;
  private _task_id:number;
  private _client_id:number;

  // constuctor

  constructor(id: number, t_date: string, t_billable: string, t_project: string, t_comment: string, t_start: string, t_end: string, t_spent: string, task_id: number, client_id: number) {
    this._id = id;
    this._t_date = t_date;
    this._t_billable = t_billable;
    this._t_project = t_project;
    this._t_comment = t_comment;
    this._t_start = t_start;
    this._t_end = t_end;
    this._t_spent = t_spent;
    this._task_id = task_id;
    this._client_id = client_id;
  }

  // getters and setters

  get id(): number {
    return this._id;
  }

  set id(value: number) {
    this._id = value;
  }

  get t_date(): string {
    return this._t_date;
  }

  set t_date(value: string) {
    this._t_date = value;
  }

  get t_billable(): string {
    return this._t_billable;
  }

  set t_billable(value: string) {
    this._t_billable = value;
  }

  get t_project(): string {
    return this._t_project;
  }

  set t_project(value: string) {
    this._t_project = value;
  }

  get t_comment(): string {
    return this._t_comment;
  }

  set t_comment(value: string) {
    this._t_comment = value;
  }

  get t_start(): string {
    return this._t_start;
  }

  set t_start(value: string) {
    this._t_start = value;
  }

  get t_end(): string {
    return this._t_end;
  }

  set t_end(value: string) {
    this._t_end = value;
  }

  get t_spent(): string {
    return this._t_spent;
  }

  set t_spent(value: string) {
    this._t_spent = value;
  }

  get task_id(): number {
    return this._task_id;
  }

  set task_id(value: number) {
    this._task_id = value;
  }

  get client_id(): number {
    return this._client_id;
  }

  set client_id(value: number) {
    this._client_id = value;
  }
}
