class Timesheet:
    timesheet_list = []

    def __init__(self, entry_no, date, billable, project, comment, start_time, end_time, time_spent, user_id, task_id, client_id):
        self.entry_no = entry_no
        self.date = date
        self.billable = billable
        self.project = project
        self.comment = comment
        self.start_time = start_time
        self.end_time = end_time
        self.time_spent = time_spent
        self.user_id = user_id
        self.task_id = task_id
        self.client_id = client_id
        timesheet_list = [self.entry_no, self.date, self.billable, self.project, self.comment, self.start_time, self.end_time, self.time_spent, self.user_id, self.task_id, self.client_id]
        Timesheet.timesheet_list.append(timesheet_list)

    @classmethod
    def get_timesheet_list(cls):
        return Timesheet.timesheet_list

    @classmethod
    def add_timesheet(cls, timesheet):
        Timesheet.timesheet_list.append(timesheet)

    @classmethod
    def remove_timesheet(cls, entry_no):
        for timesheet in Timesheet.timesheet_list:
            if timesheet[0] == entry_no:
                Timesheet.timesheet_list.remove(timesheet)
                break

    @classmethod
    def empty_timesheet_list(cls):
        Timesheet.timesheet_list = []

    def get_entry_no(self):
        return self.entry_no

    def set_entry_no(self, entry_no):
        self.entry_no = entry_no

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_billable(self):
        return self.billable

    def set_billable(self, billable):
        self.billable = billable

    def get_project(self):
        return self.project

    def set_project(self, project):
        self.project = project

    def get_comment(self):
        return self.comment

    def set_comment(self, comment):
        self.comment = comment

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def get_time_spent(self):
        return self.time_spent

    def set_time_spent(self, time_spent):
        self.time_spent = time_spent

    def get_user_id(self):
        return self.user_id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_client_id(self):
        return self.client_id

    def set_client_id(self, client_id):
        self.client_id = client_id
