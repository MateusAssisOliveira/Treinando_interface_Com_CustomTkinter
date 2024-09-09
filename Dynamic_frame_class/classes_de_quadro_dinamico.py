import customtkinter

# E para refletir o layout no código e seguir o princípio de sempre usar classes da introdução, 
# moveremos o código do frame e do checkbox para uma classe separada. 
# Esta classe herda de CTkFrame e uma instância desta classe é criada na classe principal App.
# Apenas o argumento master precisa ser passado para o método __init__ do novo MyCheckboxFrame 
# e para que ele possa então ser passado para o __init__ da superclasse que é o CTkFrame.

class MyCheckboxFrame(customtkinter.CTkFrame):
    
    def __init__(self, master, values):
        
        super().__init__(master)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
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

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self, values=["MAteus 1", "Assis 2", "Oliveira 3"]) # o Self esta referenciando a propia classe que seria o app
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        
        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())


app = App()
app.mainloop()