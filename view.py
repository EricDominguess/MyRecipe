import tkinter as tk

class View:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller
        self.root.title("My Recipe App")
        self.window_specs()
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def run(self): 
        self.main_menu_screen()
        self.root.mainloop()

    def on_close(self):
        print("Fechando a aplicação...")
        if self.root.winfo_exists():
            self.root.destroy()

    #função para definir as especificações da janela e posição
    def window_specs(self):
            #Definindo o tamanho
            width = 800
            height = 800

            background_color = "#ffffff"
            self.root.configure(bg=background_color)
            
            #Pegando o tamanho da tela do usuario
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            #Calculando a posicao x e y para centralizar a janela
            x = (screen_width // 2) - (width // 2) 
            y = (screen_height // 2) - (height // 2)

            #Definindo a geometria da janela
            self.root.geometry(f"{width}x{height}+{x}+{y}")

    #função para transição de telas
    def show_screen(self, screen_func, *args, **kwargs):
         # Limpando a tela atual
        for widget in self.root.winfo_children():
            widget.destroy()
         # Chamando a função da tela desejada
        screen_func(*args, **kwargs)

    #desenhando a tela principal
    def main_menu_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Bem vindo ao MyRecipe", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        # Botão Receitas
        recipes_btn = tk.Button(
            container, text="Receitas", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.recipes_screen)
        )
        recipes_btn.pack(fill="x", pady=(10,0))

        # Botão Adicionar Plano de Refeição
        add_meal_plan_btn = tk.Button(
            container, text="Plano de Refeição", font=("Segoe UI", 14), bg="#2196F3", fg="#ffffff",
            command=lambda: self.show_screen(self.add_meal_plan_screen)
        )
        add_meal_plan_btn.pack(fill="x", pady=(10,0))

        # Botão Ver Plano de Refeição
        view_meal_plan_btn = tk.Button(
            container, text="Ver Plano de Refeição", font=("Segoe UI", 14), bg="#3F51B5", fg="#ffffff",
            command=lambda: self.show_screen(self.meal_plan_calendar_screen)
        )
        view_meal_plan_btn.pack(fill="x", pady=(10,0))

        # Botão Editar Plano de Refeição
        edit_meal_plan_btn = tk.Button(
            container, text="Editar Plano de Refeição", font=("Segoe UI", 14), bg="#673AB7", fg="#ffffff",
            command=lambda: self.show_screen(self.edit_meal_plan_screen, plan_id=1)
        )
        edit_meal_plan_btn.pack(fill="x", pady=(10,0))

        # Botão Adicionar Receita
        add_recipe_btn = tk.Button(
            container, text="Adicionar Receita", font=("Segoe UI", 14), bg="#FF9800", fg="#ffffff",
            command=lambda: self.show_screen(self.add_recipe_screen)
        )
        add_recipe_btn.pack(fill="x", pady=(10,0))

        # Botão Editar Receita
        edit_recipe_btn = tk.Button(
            container, text="Editar Receita", font=("Segoe UI", 14), bg="#9C27B0", fg="#ffffff",
            command=lambda: self.show_screen(self.edit_recipe_screen, recipe_id=1)  # Exemplo com recipe_id fixo
        )
        edit_recipe_btn.pack(fill="x", pady=(10,0))

        # Botão Sair
        logout_btn = tk.Button(
            container, text="Sair", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.login_screen)
        )
        logout_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela de receitas
    def recipes_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Suas Receitas", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=40)
        container.pack(pady=40)

        # Tabela de receitas
        recipes_listbox = tk.Listbox(container, font=("Segoe UI", 14), bg="#F5F5F5", width=40)
        recipes_listbox.pack(fill="both", expand=True, pady=(0,15))
        
        # Exemplo de receitas
        example_recipes = [
            "Macarrão ao molho branco",
            "Frango grelhado com Batata doce",
            "Salada Caesar",
            "Bolo de chocolate",
            "Sopa de legumes"
        ]
        for recipe in example_recipes:
            recipes_listbox.insert(tk.END, recipe)

        # Função para abrir detalhes da receita ao clicar
        def on_select(event):
            selection = recipes_listbox.curselection()
            if selection:
                index = selection[0]
                recipe_name = recipes_listbox.get(index)
                # Aqui você pode passar o nome ou o id da receita
                self.show_screen(self.full_recipe_screen, recipe_name)

        recipes_listbox.bind("<<ListboxSelect>>", on_select)

        # Botão Voltar para o Menu Principal
        back_btn = tk.Button(
            container, text="Voltar para o Menu Principal", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))

    #desenhando tela de detalhes da receita
    def full_recipe_screen(self, recipe_id):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Detalhes da Receita", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        # Exemplo de detalhes da receita (substitua por seus dados)
        recipe_details = {
            "Nome": "Macarrão ao molho branco",
            "Ingredientes": "200g de macarrão\n100ml de creme de leite\n50g de queijo parmesão\nSal e pimenta a gosto",
            "Instruções": "1. Cozinhe o macarrão conforme as instruções da embalagem.\n2. Em uma panela, aqueça o creme de leite e adicione o queijo parmesão.\n3. Misture o molho ao macarrão cozido.\n4. Tempere com sal e pimenta a gosto."
        }

        # Exibindo os detalhes
        for key, value in recipe_details.items():
            key_label = tk.Label(container, text=f"{key}:", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#000000")
            key_label.pack(anchor="w", pady=(0,5))
            value_label = tk.Label(container, text=value, font=("Segoe UI", 14), bg="#F5F5F5", fg="#000000", justify="left")
            value_label.pack(fill="x", pady=(0,15))

        # Botão Excluir Receita
        delete_btn = tk.Button(
            container, text="Excluir Receita", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.recipes_screen)
        )
        delete_btn.pack(fill="x", pady=(10,0))

        # Botão Voltar para a Tela de Receitas
        back_btn = tk.Button(
            container, text="Voltar para Receitas", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.recipes_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela de adicionar receita
    def add_recipe_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Adicione sua receita ao MyRecipe", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #campo de nome da receita
        name_label = tk.Label(container, text="Nome da Receita:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        name_label.pack(anchor="w", pady=(0,5))
        name_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        name_entry.pack(fill="x", pady=(0,15))

        #campo de ingredientes
        ingredients_label = tk.Label(container, text="Ingredientes:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        ingredients_label.pack(anchor="w", pady=(0,5))
        ingredients_text = tk.Text(container, bg= "#F5F5F5", font=("Segoe UI", 14), height=5)
        ingredients_text.pack(fill="x", pady=(0,15))

        #campo de instruções
        instructions_label = tk.Label(container, text="Instruções:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        instructions_label.pack(anchor="w", pady=(0,5))
        instructions_text = tk.Text(container, bg= "#F5F5F5", font=("Segoe UI", 14), height=5)
        instructions_text.pack(fill="x", pady=(0,15))

        # Botão Adicionar Receita
        add_btn = tk.Button(
            container, text="Adicionar Receita", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        add_btn.pack(fill="x", pady=(10,0))

        # Botão Voltar para o Menu Principal
        back_btn = tk.Button(
            container, text="Voltar para o Menu Principal", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))
        
    #desenhando a tela de editar receita
    def edit_recipe_screen(self, recipe_id):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Edite sua Receita", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #campo id receita (apenas para demonstração, pode ser oculto ou removido)
        id_label = tk.Label(container, text=f"ID da Receita: {recipe_id}", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        id_label.pack(anchor="w", pady=(0,15))

        #campo de nome da receita
        name_label = tk.Label(container, text="Nome da Receita:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        name_label.pack(anchor="w", pady=(0,5))
        name_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        name_entry.pack(fill="x", pady=(0,15))

        #campo de ingredientes
        ingredients_label = tk.Label(container, text="Ingredientes:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        ingredients_label.pack(anchor="w", pady=(0,5))
        ingredients_text = tk.Text(container, bg= "#F5F5F5", font=("Segoe UI", 14), height=5)
        ingredients_text.pack(fill="x", pady=(0,15))

        #campo de instruções
        instructions_label = tk.Label(container, text="Instruções:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        instructions_label.pack(anchor="w", pady=(0,5))
        instructions_text = tk.Text(container, bg= "#F5F5F5", font=("Segoe UI", 14), height=5)
        instructions_text.pack(fill="x", pady=(0,15))

        # Botão Salvar Alterações
        save_btn = tk.Button(
            container, text="Salvar Alterações", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        save_btn.pack(fill="x", pady=(10,0))

        # Botão Voltar para o Menu Principal
        back_btn = tk.Button(
            container, text="Voltar para o Menu Principal", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela de plano de refeição
    def add_meal_plan_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Adicione Seu Plano de Refeição", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #selecionar dia da semana
        day_label = tk.Label(container, text="Selecione o Dia da Semana:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        day_label.pack(anchor="w", pady=(0,5))
        day_options = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        day_var = tk.StringVar(container)
        day_var.set(day_options[0])
        day_menu = tk.OptionMenu(container, day_var, *day_options)
        day_menu.config(font=("Segoe UI", 14), bg="#F5F5F5")
        day_menu.pack(fill="x", pady=(0,15))

        # Exemplo de receitas disponíveis
        receitas = ["Selecione", "Macarrão ao molho branco", "Frango grelhado", "Salada Caesar", "Bolo de chocolate", "Sopa de legumes"]

        # Café da manhã
        cafe_var = tk.StringVar(container)
        cafe_var.set(receitas[0])
        cafe_label = tk.Label(container, text="Café da manhã:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        cafe_label.pack(anchor="w")
        cafe_menu = tk.OptionMenu(container, cafe_var, *receitas)
        cafe_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        cafe_menu.pack(fill="x", pady=(0,5))

        # Almoço
        almoco_var = tk.StringVar(container)
        almoco_var.set(receitas[0])
        almoco_label = tk.Label(container, text="Almoço:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        almoco_label.pack(anchor="w")
        almoco_menu = tk.OptionMenu(container, almoco_var, *receitas)
        almoco_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        almoco_menu.pack(fill="x", pady=(0,5))

        # Jantar
        jantar_var = tk.StringVar(container)
        jantar_var.set(receitas[0])
        jantar_label = tk.Label(container, text="Jantar:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        jantar_label.pack(anchor="w")
        jantar_menu = tk.OptionMenu(container, jantar_var, *receitas)
        jantar_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        jantar_menu.pack(fill="x", pady=(0,15))

        # Botão Gerar Plano
        generate_btn = tk.Button(
            container, text="Gerar Plano", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        generate_btn.pack(fill="x", pady=(10,0))

        # Botão Voltar para o Menu Principal
        back_btn = tk.Button(
            container, text="Voltar para o Menu Principal", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela de visualização do plano de refeição
    def meal_plan_calendar_screen(self):
        label = tk.Label(self.root, bg="#FFFFFF", text="Calendário de Plano de Refeição", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        refeicoes = ["Café da manhã", "Almoço", "Jantar"]

        # Exemplo de plano de refeições (substitua por seus dados)
        plano = {
            "Segunda":    ["Ovos mexidos", "Frango grelhado", "Sopa de legumes"],
            "Terça":      ["Pão integral", "Peixe assado", "Salada Caesar"],
            "Quarta":     ["Iogurte", "Carne moída", "Bolo de chocolate"],
            "Quinta":     ["Frutas", "Macarrão", "Frango grelhado"],
            "Sexta":      ["Tapioca", "Salada", "Sopa de legumes"],
            "Sábado":     ["Panqueca", "Bife", "Pizza caseira"],
            "Domingo":    ["Cereal", "Lasanha", "Sanduíche natural"],
        }

        # Cabeçalho dos dias
        for col, dia in enumerate(dias):
            tk.Label(container, text=dia, font=("Segoe UI", 12, "bold"), bg="#E0E0E0", width=16, borderwidth=1, relief="solid").grid(row=0, column=col, sticky="nsew")

        # Linhas das refeições
        for row, refeicao in enumerate(refeicoes, start=1):
            for col, dia in enumerate(dias):
                texto = plano[dia][row-1] if dia in plano else ""
                tk.Label(container, text=texto, font=("Segoe UI", 12), bg="#F5F5F5", width=16, height=2, borderwidth=1, relief="solid").grid(row=row, column=col, sticky="nsew")

        # Ajusta o grid para expandir
        for col in range(len(dias)):
            container.grid_columnconfigure(col, weight=1)
        for row in range(len(refeicoes)+1):
            container.grid_rowconfigure(row, weight=1)

        # Botão Voltar
        back_btn = tk.Button(
            container, text="Voltar", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.grid(row=len(refeicoes)+1, column=0, columnspan=7, sticky="ew", pady=(20,0))    

    #desenhando a tela de editar plano de refeição
    def edit_meal_plan_screen(self, plan_id):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Adicione Seu Plano de Refeição", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #selecionar dia da semana
        day_label = tk.Label(container, text="Selecione o Dia da Semana:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        day_label.pack(anchor="w", pady=(0,5))
        day_options = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        day_var = tk.StringVar(container)
        day_var.set(day_options[0])
        day_menu = tk.OptionMenu(container, day_var, *day_options)
        day_menu.config(font=("Segoe UI", 14), bg="#F5F5F5")
        day_menu.pack(fill="x", pady=(0,15))

        # Exemplo de receitas disponíveis
        receitas = ["Selecione", "Macarrão ao molho branco", "Frango grelhado", "Salada Caesar", "Bolo de chocolate", "Sopa de legumes"]

        # Café da manhã
        cafe_var = tk.StringVar(container)
        cafe_var.set(receitas[0])
        cafe_label = tk.Label(container, text="Café da manhã:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        cafe_label.pack(anchor="w")
        cafe_menu = tk.OptionMenu(container, cafe_var, *receitas)
        cafe_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        cafe_menu.pack(fill="x", pady=(0,5))

        # Almoço
        almoco_var = tk.StringVar(container)
        almoco_var.set(receitas[0])
        almoco_label = tk.Label(container, text="Almoço:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        almoco_label.pack(anchor="w")
        almoco_menu = tk.OptionMenu(container, almoco_var, *receitas)
        almoco_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        almoco_menu.pack(fill="x", pady=(0,5))

        # Jantar
        jantar_var = tk.StringVar(container)
        jantar_var.set(receitas[0])
        jantar_label = tk.Label(container, text="Jantar:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        jantar_label.pack(anchor="w")
        jantar_menu = tk.OptionMenu(container, jantar_var, *receitas)
        jantar_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        jantar_menu.pack(fill="x", pady=(0,15))

        # Botão Salvar Plano
        save_btn = tk.Button(
            container, text="Salvar Plano", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        save_btn.pack(fill="x", pady=(10,0))

        # Botão Voltar para o Menu Principal
        back_btn = tk.Button(
            container, text="Voltar para o Menu Principal", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))  