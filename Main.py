#1. Grid System ( Sistema de grade )

#Basic App -> Aplicativo Básico 

# Primeiro de tudo, certifique-se de ter a versão mais recente do CustomTkinter instalada. 
# Então você pode testar sua instalação com o programa mais básico, que apenas cria uma janela:

import customtkinter

""" app = customtkinter.CTk()
app.mainloop() """

#Se isso estiver funcionando, você pode começar a definir propriedades da janela, como título e geometria, e começar a adicionar um botão à janela. 
# O primeiro parâmetro para qualquer widget é sempre o parâmetro master, que é app neste caso. 
# Ele também pode ser fornecido com um argumento de palavra-chave (master=app).

def button_callback():
    print("button pressed")

app = customtkinter.CTk()#Instanciando o app
app.title("my app")#Titulo da janela do app
app.geometry("400x150")# Definido as Dimiçoes da janela
app.maxsize(width=900, height=500) # O Maximo que a janela pode ser expandida pelo usuario
app.minsize(width=500, height=300) # O Minimo que a janela pode ser expandida pelo usuario

button = customtkinter.CTkButton(app, text="my button", command=button_callback)#Criando um botão com uma função button_callback

button.grid(row=0, column=0, padx=20, pady=20)



# Grid geometry manager -> Gerenciador de geometria de grade

# Neste exemplo, o gerenciador de geometria de grade é usado para definir a posição e o preenchimento do widget( São como tijolos). 
# É altamente recomendável sempre usar o gerenciador de geometria de grade em vez de colocar e empacotar, porque é muito fácil criar interfaces de usuário responsivas e extensíveis.
# A grade divide uma janela ou quadro em colunas e linhas, que se recolhem quando estão vazias, mas se adaptam ao tamanho dos widgets(Tijolo) colocados dentro delas. 
# Se você quiser centralizar o botão no último exemplo, você teria que dar à primeira coluna um peso diferente de zero, para que ela não se retraia mais 
# para o tamanho do botão (use grid_rowconfigure() para linhas):

app.grid_columnconfigure(0, weight=1) # Um valor de weight=1 significa que a coluna 0 irá expandir para ocupar todo o espaço extra disponível na horizontal.


# Agora a coluna 0 abrange toda a janela porque tem um peso de 1 e, portanto, expande. 
# Você também pode configurar o botão para expandir com sua célula de grade se você adicionar um argumento sticky à chamada de grade como este:

button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

#Agora o botão fica preso na célula da grade no lado leste e oeste. 
# Você pode notar que a célula da grade e, portanto, o tamanho do botão se adaptam se você redimensionar a janela



#Add checkboxes -> Adicionar caixas de seleção

#Para tornar o layout um pouco mais complexo, adicionamos duas caixas de seleção na segunda linha.

checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")


# Note que o argumento pady obtém uma tupla, o que significa 0 padding na parte superior e 20 padding na parte inferior. 
# Note também que as caixas de seleção são fixas apenas no lado oeste de sua célula de grade. 
# Para deixar o botão abranger a janela inteira novamente, precisamos definir um columnspan de 2 para ele (use rowspan para linhas).

button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# E para espaçar igualmente as caixas de seleção, também precisamos dar a ambas as colunas um peso igual.

app.grid_columnconfigure((0, 1), weight=1)

# Usando classes
#Para completar esta introdução, queremos estruturar este programa em uma classe. 
# É altamente recomendado usar classes que herdam de CTk para a janela principal ou CTkFrame para um quadro, 
# porque isso aumenta muito a legibilidade do código e o código se torna facilmente extensível, 
# porque as classes podem ser facilmente distribuídas para vários arquivos.




app.mainloop()