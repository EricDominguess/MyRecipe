from model import MyRecipeModel
from view import View

class Controller:
    def __init__(self):
        self.model = MyRecipeModel("MyRecipes")
        self.view = View(self)

    def run(self):
        self.view.run()

    def create_recipe_controller(self, nome, ingredientes, instrucoes):
        #Manda os Dados pro Model
        return self.model.create_recipe(nome, ingredientes, instrucoes)
    
    def get_recipe_controller(self, recipe_id):
        return self.model.get_recipe(recipe_id)
    
    def update_recipe_controller(self, recipe_id, update_data):
        return self.model.update_recipe(recipe_id, update_data)
    
    def delete_recipe_controller(self, recipe_id):
        return self.model.delete_recipe(recipe_id)
    
    def list_recipes_controller(self):
        return self.model.list_recipes()
    
    def create_meal_plan_controller(self, meal_plan_data):
        return self.model.create_meal_plan(meal_plan_data)
    
    def get_meal_plan_controller(self, meal_plan_id):   
        return self.model.get_meal_plan(meal_plan_id)