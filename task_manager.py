from user import User

class TaskManager:
    def __init__(self):
        self.users = []

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        
        new_user = User(username)
        self.users.append(new_user)
        return new_user