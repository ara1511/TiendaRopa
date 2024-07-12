from domain.user import User

class UserDAO:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None
