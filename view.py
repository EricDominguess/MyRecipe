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

    #função para transição de telas
    def show_screen(self, screen_func, *args, **kwargs):
         # Limpando a tela atual
        for widget in self.root.winfo_children():
            widget.destroy()
         # Chamando a função da tela desejada
        screen_func(*args, **kwargs)

    #desenhando a tela de login
    def login_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="MyRecipe", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #campo de usuario
        user_label = tk.Label(container, text="Usuário:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        user_label.pack(anchor="w", pady=(0,5))
        user_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        user_entry.pack(fill="x", pady=(0,15))

        #campo de senha
        pass_label = tk.Label(container, text="Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        pass_label.pack(anchor="w", pady=(0,5))
        pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        pass_entry.pack(fill="x", pady=(0,15))
        
        # Botão Entrar
        login_btn = tk.Button(
            container, text="Entrar", font=("Segoe UI", 14), bg="#4CAF50", fg="#ffffff",
            command=lambda: self.show_screen(self.main_menu_screen)
        )
        login_btn.pack(fill="x", pady=(10,0))

        # Botão Registrar
        register_btn = tk.Button(
            container, text="Registrar", font=("Segoe UI", 14), bg="#2196F3", fg="#ffffff",
            command=lambda: self.show_screen(self.register_screen)
        )
        register_btn.pack(fill="x", pady=(10,0))

        # Botão Esqueci a senha
        forgot_btn = tk.Button(
            container, text="Esqueci a senha", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.forgot_password_screen)
        )
        forgot_btn.pack(fill="x", pady=(10,0))

    #desenhando a tela de registro
    def register_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Registrar", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        #campo de usuario
        user_label = tk.Label(container, text="Usuário:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        user_label.pack(anchor="w", pady=(0,5))
        user_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        user_entry.pack(fill="x", pady=(0,15))

        #campo de senha
        pass_label = tk.Label(container, text="Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        pass_label.pack(anchor="w", pady=(0,5))
        pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        pass_entry.pack(fill="x", pady=(0,15))

        #campo de confirmar senha
        confirm_pass_label = tk.Label(container, text="Confirmar Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        confirm_pass_label.pack(anchor="w", pady=(0,5))
        confirm_pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        confirm_pass_entry.pack(fill="x", pady=(0,15))
        
        # Botão Registrar
        register_btn = tk.Button(
            container, text="Registrar", font=("Segoe UI", 14), bg="#2196F3", fg="#ffffff",
            command=lambda: self.show_screen(self.login_screen)
        )
        register_btn.pack(fill="x", pady=(10,0))

        #botão voltar para o login
        back_btn = tk.Button(
            container, text="Voltar para o Login", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.login_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))

    #desenhando a tela de esqueci a senha
    def forgot_password_screen(self):
        label = tk.Label(self.root, bg= "#FFFFFF", text="Esqueci a senha", font=("Segoe UI", 22, "bold"))
        label.pack(pady=20)

        container = tk.Frame(self.root, bg="#FFFFFF", padx=30, pady=30)
        container.pack(pady=40)

        label_info = tk.Label(container, text="Insira seu usuário, nova senha e o código de verificação ", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        label_info.pack(anchor="w", pady=(0,15))

        #campo de código
        code_label = tk.Label(container, text="Código de Verificação:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        code_label.pack(anchor="w", pady=(0,5))
        code_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        code_entry.pack(fill="x", pady=(0,15))

        #campo de usuario
        user_label = tk.Label(container, text="Usuário:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        user_label.pack(anchor="w", pady=(0,5))
        user_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14))
        user_entry.pack(fill="x", pady=(0,15))

        #campo de nova senha
        new_pass_label = tk.Label(container, text="Nova Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        new_pass_label.pack(anchor="w", pady=(0,5))
        new_pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        new_pass_entry.pack(fill="x", pady=(0,15))

        #campo de confirmar nova senha
        confirm_pass_label = tk.Label(container, text="Confirmar Nova Senha:", font=("Segoe UI", 14), bg="#FFFFFF", fg="#000000")
        confirm_pass_label.pack(anchor="w", pady=(0,5))
        confirm_pass_entry = tk.Entry(container, bg= "#F5F5F5", font=("Segoe UI", 14), show="*")
        confirm_pass_entry.pack(fill="x", pady=(0,15))

        # Botão Redefinir Senha
        reset_btn = tk.Button(
            container, text="Redefinir Senha", font=("Segoe UI", 14), bg="#2196F3", fg="#ffffff",
            command=lambda: self.show_screen(self.login_screen)
        )
        reset_btn.pack(fill="x", pady=(10,0))

        #botão voltar para o login
        back_btn = tk.Button(
            container, text="Voltar para o Login", font=("Segoe UI", 14), bg="#f44336", fg="#ffffff",
            command=lambda: self.show_screen(self.login_screen)
        )
        back_btn.pack(fill="x", pady=(10,0))
    
    #desenhando a tela principal
    def main_menu_screen(self):
        pass
    
    #desenhando a tela de receitas
    def recipes_screen(self):
        pass
    
    #desenhando a tela de adicionar receita
    def add_recipe_screen(self):
        pass
    
    #desenhando a tela de editar receita
    def edit_recipe_screen(self, recipe_id):
        pass
    
    #desenhando a tela de plano de refeição
    def meal_plan_screen(self):
        pass
        
        
if __name__ == "__main__":
        view = View(None)    