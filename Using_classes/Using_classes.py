import customtkinter  # Importa a biblioteca customtkinter, que é uma extensão para o tkinter com widgets personalizados.

# A seguir, definimos uma classe personalizada para agrupar e organizar widgets relacionados.
class MyCheckboxFrame(customtkinter.CTkFrame):
    
    def __init__(self, master):
        # O método __init__ inicializa a nova instância da classe.
        # Chama o método __init__ da superclasse (CTkFrame) para garantir que a estrutura da base seja configurada corretamente.
        super().__init__(master)

        # Cria um widget de checkbox, associado ao frame atual, com o texto "checkbox 1".
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # Organiza o checkbox_1 usando o layout grid: linha 0, coluna 0, com margens internas (padx e pady) e alinhamento à esquerda.
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        
        # Cria um segundo widget de checkbox, associado ao frame atual, com o texto "checkbox 2".
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # Organiza o checkbox_2 usando o layout grid: linha 1, coluna 0, com margens internas (padx e pady) e alinhamento à esquerda.
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

# Define a classe principal da aplicação que herda de CTk (uma extensão do tkinter que permite uma interface personalizada).
class App(customtkinter.CTk):
    
    def __init__(self):
        # O método __init__ inicializa a nova instância da classe.
        # Chama o método __init__ da superclasse (CTk) para garantir que a estrutura da base seja configurada corretamente.
        super().__init__()

        # Define o título da janela da aplicação.
        self.title("my app")
        # Define o tamanho da janela da aplicação.
        self.geometry("400x180")
        # Configura a coluna 0 do grid para expandir e ocupar o espaço disponível.
        self.grid_columnconfigure(0, weight=1)
        # Configura a linha 0 do grid para expandir e ocupar o espaço disponível.
        self.grid_rowconfigure(0, weight=1)

        # Cria uma instância da classe MyCheckboxFrame, passando a instância atual de App como o master.
        self.checkbox_frame = MyCheckboxFrame(self) 
        # Organiza o frame de checkboxes usando o layout grid: linha 0, coluna 0, com margens internas (padx e pady) e alinhamento ao nordeste.
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # Cria um botão, associado à instância atual de App, com o texto "my button" e a função de callback definida para quando o botão for pressionado.
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # Organiza o botão usando o layout grid: linha 3, coluna 0, com margens internas (padx e pady) e alinhamento leste-oeste.
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    # Define a função de callback que será chamada quando o botão for pressionado.
    def button_callback(self):
        print("button pressed")  # Imprime uma mensagem no console quando o botão for pressionado.

# Cria uma instância da classe App e inicia o loop principal da aplicação, que mantém a janela aberta e responde a eventos.
app = App()
app.mainloop()
