# Interface gráfica
# Importa a biblioteca do tkinter
from tkinter import *
import tkinter
  
value = True
windows_main = tkinter.Tk(className="Inteface graphic - Bolão", )

# Centralizando a screen
windows_main.resizable(False, False)  # This code helps to disable windows from resizing

window_height = 800
window_width = 1200

screen_width = windows_main.winfo_screenwidth()
screen_height = windows_main.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

windows_main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Insere o nome da janela
windows_main.title("Interface Bolão")

# Campo de entrada de dados
# texto lateral usando grid com posicionamento de colunas e linhas
Label(windows_main, text="Número da cartela").grid(row=0)
Label(windows_main, text="Nome").grid(row=1)
Label(windows_main, text="Endereço").grid(row=2)

# label de entrada
#bd = border, bg = background-color
card_number = Entry(windows_main, bd=3, bg="#f1f1f1", width=40).grid(row=0, column= 1)
player_name = Entry(windows_main).grid(row=1, column= 1)
adress_player = Entry(windows_main).grid(row=2, column= 1)
start_data = Entry(windows_main).grid(row=3, column=1)

# Botão de enserir os dados das pessoas na tabela
insert_code_table = Button(windows_main, activebackground="#1f1f1f", text="Insert person", width=20, command=windows_main.destroy)
#insert_code_table.pack()

windows_main.mainloop()