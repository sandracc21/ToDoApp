class BaseTask:
    def __init__(self, title, time):
        self.title = title
        self.time = time  
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def display(self):
        status = "Completed" if self.completed else "Incomplete"
        print(f"{self.title} is {status} (Due: {self.time})")