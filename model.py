from pymongo import MongoClient

class MyRecipeModel:
    def __init__(self, db_name, connection_uri="mongodb://localhost:27017/"):
        self.client = MongoClient(connection_uri)
        self.db = self.client[db_name]
        self.collection = self.db["recipes"]
        self.users_collection = self.db["users"]
        self.counter_collection = self.db["counters"]

    # Inicializa o contador para IDs de receitas sequenciais
    def initialize_counter(self):
        if self.counter_collection.count_documents({"_id": "recipe_id"}) == 0:
            self.counter_collection.insert_one({"_id": "recipe_id", "seq": 0})
    
    # Incrementa e retorna o próximo valor do contador
    def get_next_sequence(self):
        result = self.counter_collection.find_one_and_update(
            {"_id": "recipe_id"},
            {"$inc": {"seq": 1}},
            return_document=True
        )
        return result["seq"]
    
    # Cria uma nova receita
    def create_recipe(self, recipe_data):
        # Insere uma nova receita no banco de dados
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
    
    # Cria um novo usuário
    def create_user(self, user_data):
        result = self.users_collection.insert_one(user_data)
        return result.inserted_id
    
    # Verifica as credenciais do usuário para login
    def login_user(self, username, password):
        user = self.users_collection.find_one({"username": username, "password": password})
        return user is not None
    
    def login_status(self, username):
        pass

    def verification_code(self, email):
        pass
    
    # Desloga o usuário randomizando o código de verificação
    def logout_user(self, username):
        pass