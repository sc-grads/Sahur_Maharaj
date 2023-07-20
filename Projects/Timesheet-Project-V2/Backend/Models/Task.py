class Task:
    task_list = []

    def __init__(self, task_id, task_name, task_description):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        task_list = [self.task_id, self.task_name, self.task_description]
        Task.task_list.append(task_list)

    @classmethod
    def get_task_list(cls):
        return Task.task_list

    @classmethod
    def add_task(cls, task):
        Task.task_list.append(task)

    @classmethod
    def remove_task(cls, task_id):
        for task in Task.task_list:
            if task[0] == task_id:
                Task.task_list.remove(task)
                break

    @classmethod
    def empty_task_list(cls):
        Task.task_list = []

    def get_task_id(self):
        return self.task_id

    def set_task_id(self, task_id):
        self.task_id = task_id

    def get_task_name(self):
        return self.task_name

    def set_task_name(self, task_name):
        self.task_name = task_name

    def get_task_description(self):
        return self.task_description

    def set_task_description(self, task_description):
        self.task_description = task_description
