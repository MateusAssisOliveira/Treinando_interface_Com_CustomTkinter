import customtkinter

# E para refletir o layout no código e seguir o princípio de sempre usar classes da introdução, 
# moveremos o código do frame e do checkbox para uma classe separada. 
# Esta classe herda de CTkFrame e uma instância desta classe é criada na classe principal App.
# Apenas o argumento master precisa ser passado para o método __init__ do novo MyCheckboxFrame 
# e para que ele possa então ser passado para o __init__ da superclasse que é o CTkFrame.

class MyCheckboxFrame(customtkinter.CTkFrame):
    
    def __init__(self, master):
        
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

class App(customtkinter.CTk):
    
    def __init__(self):
        
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self) # o Self esta referenciando a propia classe que seria o app
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()