#1. Grid System ( Sistema de grade )

#Basic App -> Aplicativo Básico 

# Primeiro de tudo, certifique-se de ter a versão mais recente do CustomTkinter instalada. 
# Então você pode testar sua instalação com o programa mais básico, que apenas cria uma janela:

import customtkinter

app = customtkinter.CTk()
app.mainloop()

#Se isso estiver funcionando, você pode começar a definir propriedades da janela, como título e geometria, e começar a adicionar um botão à janela. 
# O primeiro parâmetro para qualquer widget é sempre o parâmetro master, que é app neste caso. 
# Ele também pode ser fornecido com um argumento de palavra-chave (master=app).

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("my app")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()