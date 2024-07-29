import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        
        # Se agora quisermos adicionar outra caixa de seleção na linha 2, também teremos que alterar o número da linha do botão. 
        # Então, uma alteração como essa requer alterações no layout abaixo da caixa de seleção. 
        # Para evitar esses efeitos colaterais, manter as alterações contidas e estruturar o layout visualmente, estamos usando frames. 
        # Colocamos o frame na linha 0, o botão na linha 1 e configuramos a linha 0 e a coluna 0 para expandir. 
        # O frame recebe um parâmetro fixo de 'nsw' para que ele se expanda com sua célula para o norte, sul e oeste. 
        # As caixas de seleção agora recebem o frame como o argumento mestre em vez de self.
        

        self.checkbox_frame = customtkinter.CTkFrame(self) # Criando o frame [ Box Fantasma]   
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw") # Inserindo Na nossa grid
        
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1") # Craindo o checkbox 1
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w") # Inserindo o checkbox na nssa grid que ira ficar dentro do frame na linha 0 e coluna 0
        
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")# Craindo o checkbox 2
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")# Inserindo o checkbox na nssa grid que ira ficar dentro do frame na linha 1 e coluna 0

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback) # Criando o btn 
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")  # Inserindo o btn na grid fota do frame

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()