from model import MyRecipeModel
from view import View

class Controller:
    def __init__(self):
        self.model = MyRecipeModel("MyRecipes")
        self.view = View(self)

    def run(self):
        self.view.run()

    def create_recipe_controller(self, nome, ingredientes, instrucoes):
        # Manda os dados da receita pro Model
        return self.model.create_recipe(nome, ingredientes, instrucoes)
    
    def get_recipe_controller(self, recipe_id):
        return self.model.get_recipe(recipe_id)
    
    def update_recipe_controller(self, recipe_id, name, ingredients, instructions):
        # Monta o dicionário com os dados atualizados
        update_data = {
            "Nome": name,
            "Ingredientes": ingredients,
            "Instrucoes": instructions
        }
        # Passa para o model executar a atualização
        return self.model.update_recipe(recipe_id, update_data)
    
    def delete_recipe_controller(self, recipe_id):
        return self.model.delete_recipe(recipe_id)
    
    def list_recipes_controller(self):
        return self.model.list_recipes()
    
    def unlink_recipe_from_meal_plans_controller(self, recipe_name):
        return self.model.unlink_recipe_from_meal_plans(recipe_name)

    def save_meal_plan_controller(self, dia, cafe, almoco, jantar):
        # Chama função do model
        result = self.model.save_meal_plan(dia, cafe, almoco, jantar)

        # Feedback da operação
        if result.upserted_id:
            # Se upserted_id não for nulo, um novo documento foi CRIADO.
            return "created"
        elif result.modified_count > 0:
            # Se modified_count for maior que 0, um documento existente foi ATUALIZADO.
            return "updated"
        elif result.matched_count > 0 and result.modified_count == 0:
            # Se encontrou um documento mas não modificou nada
            return "no_change"
        else:
            return "failed"
    
    def list_meal_plans_controller(self):
        return self.model.list_meal_plans()