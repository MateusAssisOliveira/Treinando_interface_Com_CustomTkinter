import customtkinter

# E para refletir o layout no código e seguir o princípio de sempre usar classes da introdução, 
# moveremos o código do frame e do checkbox para uma classe separada. 
# Esta classe herda de CTkFrame e uma instância desta classe é criada na classe principal App.
# Apenas o argumento master precisa ser passado para o método __init__ do novo MyCheckboxFrame 
# e para que ele possa então ser passado para o __init__ da superclasse que é o CTkFrame.

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []
        """ 
        
        Parâmetros:
            CTkLabel
            -> master: O widget pai.
            -> width, height, corner_radius: Dimensões e raio dos cantos arredondados.
            -> bg_color, fg_color, text_color, text_color_disabled: Cores de fundo, primeiro plano e texto.
            -> text: Texto a ser exibido.
            -> font: Fonte usada no texto.
            -> image: Imagem a ser exibida.
            -> compound, anchor, wraplength: Configurações adicionais para o texto e layout.
        
        
        """
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
        
class App(customtkinter.CTk):
    
    def __init__(self):
        
        super().__init__()

        #Caracteristicas da janla do app
        self.title("my app") # Titulo
        self.geometry("400x180") # Dimenção
        
        """ 
        grid_columnconfigure((0, 1), weight=1) 
        
        Configurção da coluna (0, 1): Essa é a tupla que especifica as colunas que estão sendo configuradas (no caso, a coluna 0 e a coluna 1).
        
        weight=1: O peso (weight) é usado para determinar como o espaço adicional (quando a janela é redimensionada) será distribuído entre as 
        colunas. Quando duas colunas têm o mesmo peso, elas compartilharão o espaço adicional de maneira igual. 
        Se uma coluna tivesse weight=2, ela receberia o dobro do espaço da coluna com weight=1.
        
        """
        self.grid_columnconfigure((0, 1), weight=1) # Configurção da coluna  App
        
        """ 
        self.grid_rowconfigure(0): Refere-se à linha 0 do layout de grade dentro do widget no qual você está chamando esse método
        
        weight=1: O argumento weight define a "prioridade" com que essa linha será redimensionada em relação a outras linhas quando o 
        layout mudar (como quando a janela é redimensionada). O weight=1 significa que essa linha será redimensionada proporcionalmente 
        ao espaço disponível. Se todas as linhas configuradas tiverem o mesmo peso, elas se expandirão ou contrairão igualmente. 
        Linhas com pesos maiores receberão mais espaço.
        
        
        """
        self.grid_rowconfigure(0, weight=1)# Configurção da linha App

        # Construinfo o frame
        self.checkbox_frame_1 = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])


        self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew") # Definindo as caracreristiscas do grid
        
        # Construinfo o frame
        self.checkbox_frame_2 = MyCheckboxFrame(self, "Options", values=["option 1", "option 2"])
        self.checkbox_frame_2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="nsew") # Definindo as caracreristiscas do grid
        
        
        #Contruindo o bontão de ação 
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew",columnspan=2)

    def button_callback(self):
        print("checkbox_frame_1:", self.checkbox_frame.get())
        print("checkbox_frame_2:", self.checkbox_frame_2.get())


app = App()
app.mainloop()