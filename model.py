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
    
    def unlink_recipe_from_meal_plans(self, recipe_name):
        # Filtro para encontrar todos os planos que usam a receita
        filtro = {
            "$or": [
                {"refeicoes.cafe_da_manha": recipe_name},
                {"refeicoes.almoco": recipe_name},
                {"refeicoes.jantar": recipe_name}
            ]
        }
        
        # Busca todos os planos que correspondem ao filtro
        plans_to_update = list(self.db["meal_plans"].find(filtro))

        # Itera sobre cada plano encontrado
        for plan in plans_to_update:
            refeicoes = plan["refeicoes"]
            # Verifica e substitui o nome da receita em cada tipo de refeição
            if refeicoes.get("cafe_da_manha") == recipe_name:
                refeicoes["cafe_da_manha"] = "[Receita Excluída]"
            if refeicoes.get("almoco") == recipe_name:
                refeicoes["almoco"] = "[Receita Excluída]"
            if refeicoes.get("jantar") == recipe_name:
                refeicoes["jantar"] = "[Receita Excluída]"
            
            # Atualiza o documento no banco de dados
            self.db["meal_plans"].update_one({"_id": plan["_id"]}, {"$set": {"refeicoes": refeicoes}})

        return True

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
    
    def save_meal_plan(self, dia, cafe, almoco, jantar):
        # Filtro para encontrar o plano pelo dia da semana
        filtro = {"dia_da_semana": dia}

        # Dados de Atualização
        # "$set" sendo usado para definir os novos valores.
        novos_dados = {
            "$set": {
                "dia_da_semana": dia, 
                "refeicoes": {
                    "cafe_da_manha": cafe,
                    "almoco": almoco,
                    "jantar": jantar
                }
            }
        }

        # O update_one procura pelo filtro. Se achar, aplica os novos_dados.
        result = self.db["meal_plans"].update_one(filtro, novos_dados, upsert=True)
        
        # Retornamos o objeto de resultado para o controller poder inspecioná-lo
        return result
        
    def list_meal_plans(self):
        return list(self.db["meal_plans"].find())