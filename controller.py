from model import MyRecipeModel
from view import View

class Controller:
    def __init__(self):
        self.model = MyRecipeModel("MyRecipes")
        self.view = View(self)

    def run(self):
        self.view.login_screen()
