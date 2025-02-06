from task import Task

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, title, time):
        new_task = Task(title, time)
        self.tasks.append(new_task)

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]

    def display_tasks(self):
        for task in self.tasks:
            task.display()

    def filter_tasks(self, completed=True):
        return [task for task in self.tasks if task.completed == completed]

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None