import tkinter as tk
from tkinter import messagebox

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

    #função para adicionar receita
    def handle_add_recipe(self, name_entry, ingredients_text, instructions_text):
        nome = name_entry.get()
        ingredientes = ingredients_text.get("1.0", tk.END).strip()
        instrucoes = instructions_text.get("1.0", tk.END).strip()

        # A validação para conferir se todos os campos foram preenchidos
        if not nome or not ingredientes or not instrucoes:
            messagebox.showerror("Erro de Validação", "Todos os campos devem ser preenchidos!")
            return

        #Chamando o controller passando os dados
        try:
            recipe_id = self.controller.create_recipe_controller(nome, ingredientes, instrucoes)
            
            if recipe_id:
                messagebox.showinfo("Sucesso", f"Receita '{nome}' adicionada com sucesso!")
                # Limpa os campos e volta para o menu
                name_entry.delete(0, tk.END)
                ingredients_text.delete("1.0", tk.END)
                instructions_text.delete("1.0", tk.END)
                self.show_screen(self.main_menu_screen)
            else:
                messagebox.showerror("Erro no Banco", "Não foi possível adicionar a receita.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar a receita: {e}")

    #função para adicionar plano de refeição
    def handle_add_meal_plan(self, day_var, cafe_var, almoco_var, jantar_var):
        dia = day_var.get()
        cafe = cafe_var.get()
        almoco = almoco_var.get()
        jantar = jantar_var.get()

        if cafe == "Selecione" or almoco == "Selecione" or jantar == "Selecione":
            messagebox.showerror("Erro de Validação", "Você deve selecionar uma receita para cada refeição.")
            return

        try:
            # Chama função do controller
            status = self.controller.save_meal_plan_controller(dia, cafe, almoco, jantar)

            # Feedback mostrando a mensagem apropriada
            if status == "created":
                messagebox.showinfo("Sucesso", f"Plano de refeição para '{dia}' foi criado com sucesso!")
            elif status == "updated":
                messagebox.showinfo("Sucesso", f"Plano de refeição para '{dia}' foi atualizado com sucesso!")
            elif status == "no_change":
                messagebox.showinfo("Informação", f"O plano de refeição para '{dia}' não precisou de alterações.")
            else:
                messagebox.showerror("Erro no Banco", "Não foi possível salvar o plano de refeição.")
                return 

            self.show_screen(self.main_menu_screen)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar o plano: {e}")

    #função para deletar receita
    def handle_delete_recipe(self, recipe_id, recipe_name):
        # Pedir confirmação ao usuário antes de excluir
        confirm = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Tem certeza de que deseja excluir a receita '{recipe_name}'?\n\nEsta ação não pode ser desfeita."
        )

        # Se confirmou, prosseguir com a exclusão
        if confirm:
            try:

                # Primeiro, desvincula a receita de quaisquer planos de refeição
                self.controller.unlink_recipe_from_meal_plans_controller(recipe_name)

                # Chama o controller para deletar a receita pelo ID
                deleted_count = self.controller.delete_recipe_controller(recipe_id)

                # O model retorna o número de itens deletados
                if deleted_count > 0:
                    messagebox.showinfo("Sucesso", f"A receita '{recipe_name}' foi excluída com sucesso.")
                    self.show_screen(self.recipes_screen)
                else:
                    messagebox.showerror("Erro", "A receita não foi encontrada no banco de dados e não pôde ser excluída.")

            except Exception as e:
                messagebox.showerror("Erro de Execução", f"Ocorreu um erro ao tentar excluir a receita: {e}")

    #função para definir as especificações da janela e posição
    def window_specs(self):
            #Definindo o tamanho
            width = 1200
            height = 1000

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
        exit_btn = tk.Button(
            container, text="Sair", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.root.destroy()
        )
        exit_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela de receitas
    def recipes_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Suas Receitas", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=40)
        container.pack(pady=40)

        # Tabela de receitas
        recipes_listbox = tk.Listbox(container, font=("Segoe UI", 14), bg="#F5F5F5", width=40)
        recipes_listbox.pack(fill="both", expand=True, pady=(0,15))
        
        self.recipe_list_data = []

        try:
            # Busca todas as receitas do banco de dados
            self.recipe_list_data = self.controller.list_recipes_controller()

            if self.recipe_list_data:
                # Puxa os nomes das receitas
                for recipe in self.recipe_list_data:
                    recipes_listbox.insert(tk.END, recipe.get("Nome", "Receita sem nome"))
            else:
                recipes_listbox.insert(tk.END, "Nenhuma receita encontrada.")

        except Exception as e:
            recipes_listbox.insert(tk.END, "Erro ao carregar receitas.")
            print(f"Ocorreu um erro ao carregar receitas: {e}")


        def on_select(event):
            selection_indices = recipes_listbox.curselection()
            if selection_indices:
                # Pega o índice do primeiro item selecionado
                index = selection_indices[0]
                # Usa o índice para encontrar a receita correspondente na nossa lista de dados
                selected_recipe = self.recipe_list_data[index]
                recipe_id = selected_recipe['_id']
                self.show_screen(self.full_recipe_screen, recipe_id)

        # Associa a função de seleção da Listbox
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
        container.pack(pady=40, fill="both", expand=True)

        try:
            # Busca os detalhes da receita específica pelo ID
            recipe_details = self.controller.get_recipe_controller(recipe_id)

            if recipe_details:

                # Exibir o Nome
                nome_content = recipe_details.get("Nome", "Não informado")
                nome_key_label = tk.Label(container, text="Nome:", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#000000", anchor="w")
                nome_key_label.pack(fill="x", pady=(10, 2))
                nome_value_label = tk.Label(container, text=nome_content, font=("Segoe UI", 14), bg="#F5F5F5", fg="#000000", justify="left", wraplength=600)
                nome_value_label.pack(fill="x", pady=(0, 15))

                # Exibir os Ingredientes
                ingredientes_content = recipe_details.get("Ingredientes", "Não informado")
                ingredientes_key_label = tk.Label(container, text="Ingredientes:", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#000000", anchor="w")
                ingredientes_key_label.pack(fill="x", pady=(10, 2))
                ingredientes_value_label = tk.Label(container, text=ingredientes_content, font=("Segoe UI", 14), bg="#F5F5F5", fg="#000000", justify="left", wraplength=600)
                ingredientes_value_label.pack(fill="x", pady=(0, 15))

                # Exibir as Instruções
                instrucoes_content = recipe_details.get("Instrucoes", "Não informado")
                instrucoes_key_label = tk.Label(container, text="Instruções:", font=("Segoe UI", 14, "bold"), bg="#FFFFFF", fg="#000000", anchor="w")
                instrucoes_key_label.pack(fill="x", pady=(10, 2))
                instrucoes_value_label = tk.Label(container, text=instrucoes_content, font=("Segoe UI", 14), bg="#F5F5F5", fg="#000000", justify="left", wraplength=600)
                instrucoes_value_label.pack(fill="x", pady=(0, 15))

            else:
                tk.Label(container, text="Receita não encontrada.", font=("Segoe UI", 14)).pack()

        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar os detalhes da receita: {e}")
            self.show_screen(self.recipes_screen)

        # Botão Excluir Receita
        delete_btn = tk.Button(
                container, text="Excluir Receita", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
                # O comando agora chama nossa nova função, passando o ID e o nome da receita
                command=lambda: self.handle_delete_recipe(recipe_id, nome_content)
            )
        delete_btn.pack(fill="x", pady=(20,0))

        # Botão Voltar para a Tela de Receitas
        back_btn = tk.Button(
            container, text="Voltar para Receitas", font=("Segoe UI", 14), bg="#607D8B", fg="#ffffff",
            command=lambda: self.show_screen(self.recipes_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))

    #desenhando a tela de editar receita
    def edit_recipe_screen(self, recipe_id):
        pass

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
            # E o comando dele CHAMA o outro método da classe
            command=lambda: self.handle_add_recipe(name_entry, ingredients_text, instructions_text)
        )
        add_btn.pack(fill="x", pady=(10,0))

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

        # Buscar as receitas no banco de dados
        try:
            # Chama o controller para obter a lista de todas as receitas
            all_recipes = self.controller.list_recipes_controller()
            
            # Extrai apenas os nomes das receitas da lista de dicionários
            recipe_names = [recipe.get("Nome", "Receita sem nome") for recipe in all_recipes]

        except Exception as e:
            messagebox.showerror("Erro de Conexão", f"Não foi possível carregar as receitas do banco de dados: {e}")
            recipe_names = []

        # Preparar a lista de opções para os menus suspensos
        opcoes_receitas = ["Selecione"] + recipe_names
        
        # Se nenhuma receita foi encontrada, deixa uma mensagem 
        if not recipe_names:
            opcoes_receitas = ["Nenhuma receita cadastrada"]

        #selecionar dia da semana
        day_label = tk.Label(container, text="Selecione o Dia da Semana:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        day_label.pack(anchor="w", pady=(0,5))
        day_options = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        day_var = tk.StringVar(container)
        day_var.set(day_options[0])
        day_menu = tk.OptionMenu(container, day_var, *day_options)
        day_menu.config(font=("Segoe UI", 14), bg="#F5F5F5")
        day_menu.pack(fill="x", pady=(0,15))

        # Café da manhã (agora usa a lista dinâmica 'opcoes_receitas')
        cafe_var = tk.StringVar(container)
        cafe_var.set(opcoes_receitas[0])
        cafe_label = tk.Label(container, text="Café da manhã:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        cafe_label.pack(anchor="w")
        cafe_menu = tk.OptionMenu(container, cafe_var, *opcoes_receitas) # <--- MUDANÇA AQUI
        cafe_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        cafe_menu.pack(fill="x", pady=(0,5))

        # Almoço (agora usa a lista dinâmica 'opcoes_receitas')
        almoco_var = tk.StringVar(container)
        almoco_var.set(opcoes_receitas[0])
        almoco_label = tk.Label(container, text="Almoço:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        almoco_label.pack(anchor="w")
        almoco_menu = tk.OptionMenu(container, almoco_var, *opcoes_receitas) # <--- MUDANÇA AQUI
        almoco_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        almoco_menu.pack(fill="x", pady=(0,5))

        # Jantar (agora usa a lista dinâmica 'opcoes_receitas')
        jantar_var = tk.StringVar(container)
        jantar_var.set(opcoes_receitas[0])
        jantar_label = tk.Label(container, text="Jantar:", font=("Segoe UI", 12), bg="#FFFFFF", fg="#000000")
        jantar_label.pack(anchor="w")
        jantar_menu = tk.OptionMenu(container, jantar_var, *opcoes_receitas) # <--- MUDANÇA AQUI
        jantar_menu.config(font=("Segoe UI", 12), bg="#F5F5F5")
        jantar_menu.pack(fill="x", pady=(0,15))

        # Botão Gerar Plano (a lógica dele continua a mesma e vai funcionar)
        generate_btn = tk.Button(
            container, text="Gerar Plano", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.handle_add_meal_plan(day_var, cafe_var, almoco_var, jantar_var)
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