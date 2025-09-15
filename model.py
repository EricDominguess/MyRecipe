from pymongo import MongoClient

class MyRecipeModel:
    def __init__(self, db_name, connection_uri="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_uri)
        self.db = self.client[db_name]
        self.collection = self.db["recipes"]
    
    # Cria uma nova receita
    def create_recipe(self, nome, ingredientes, instrucoes):
        recipe_data = {
            "Nome": nome,
            "Ingredientes": ingredientes,
            "Instrucoes": instrucoes
        }
        
        # Insere o dicionário já formatado no banco de dados
        result = self.collection.insert_one(recipe_data)
        return result.inserted_id

    # Busca uma receita pelo ID no banco de dados
    def get_recipe(self, recipe_id):
        # Recupera uma receita pelo ID
        return self.collection.find_one({"_id": recipe_id})
    
    # Atualiza uma receita existente
    def update_recipe(self, recipe_id, update_data):
        result = self.collection.update_one({"_id": recipe_id}, {"$set": update_data})
        return result.modified_count
    
    # Deleta uma receita pelo ID
    def delete_recipe(self, recipe_id):
        result = self.collection.delete_one({"_id": recipe_id})
        return result.deleted_count
    
    # Lista todas as receitas
    def list_recipes(self):
        return list(self.collection.find())
    
    def create_meal_plan(self, meal_plan_data):
        result = self.db["meal_plans"].insert_one(meal_plan_data)
        return result.inserted_id
    
    def get_meal_plan(self, meal_plan_id):
        return self.db["meal_plans"].find_one({"_id": meal_plan_id})
    
