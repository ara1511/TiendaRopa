from dao.user_dao import UserDAO
from service.singleton import Singleton

class UserService(metaclass=Singleton):
    def __init__(self):
        self.user_dao = UserDAO()

    def add_user(self, user):
        self.user_dao.add_user(user)

    def get_all_users(self):
        return self.user_dao.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_dao.get_user_by_id(user_id)
