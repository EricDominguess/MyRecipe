from model import UserModel
from view import View

class Controller:
    def __init__(self):
        self.model = UserModel()
        self.view = View(self)