import tkinter as tk

class View:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller
        self.root.title("My Recipe App")
        self.window_specs()
        self.login_screen()
        self.root.mainloop()

    #função para definir as especificações da janela e posição
    def window_specs(self):
            #Definindo o tamanho
            width = 800
            height = 600

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

    #desenhando a tela de login
    def login_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Welcome to MyRecipe", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #estruturando o campo de usuario
        user_label = tk.Label(container, text="Usuário:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        user_label.pack(anchor="w", pady=(0,5))
        user_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        user_entry.pack(fill="x", pady=(0,15))

        pass_label = tk.Label(container, text="Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        pass_label.pack(anchor="w", pady=(0,5))
        pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        pass_entry.pack(fill="x", pady=(0,15))

        login_btn = tk.Button(container, text="Entrar", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff")
        login_btn.pack(fill="x", pady=(10,0))
        
    def register_screen(self):
        pass

    def recipes_screen(self):
        pass

    def add_recipe_screen(self):
        pass

    def edit_recipe_screen(self, recipe_id):
        pass

    def meal_plan_screen(self):
        pass
        
        
if __name__ == "__main__":
        view = View(None)    