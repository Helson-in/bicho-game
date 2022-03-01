<<<<<<< HEAD
# Interface gráfica
# Importa a biblioteca do tkinter
from logging import root
from textwrap import fill
from tkinter import *
import tkinter
from tokenize import String
from turtle import left, width
from typing import Container
  
def limitar_tamanho(p):
    if len(p) > 2:
        return False
    return True

value = True
windows_main = tkinter.Tk(className="Inteface graphic - Bolão", )

vcmd = windows_main.register(func=limitar_tamanho)
  

# Insere o nome da janela
windows_main.title("Interface Bolão")

# Centralizando a screen
windows_main.resizable(False, False)  # Desativa o reajuste de tela padrão do windows

window_height = 170 # altura da janela
window_width = 550 # largura da janela

screen_width = windows_main.winfo_screenwidth() # retorna a largura da tela
screen_height = windows_main.winfo_screenheight() # retorna a altura da tela

x_cordinate = int((screen_width/2) - (window_width/2)) # posição central
y_cordinate = int((screen_height/2) - (window_height/2)) # posição central

windows_main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) # Gerência o tamanho da tela

# cor de fundo
windows_main.configure(background="white")

# Frame de dados do usuário
player_data_frame = Frame(windows_main)
player_data_frame.pack(expand=True, side="left")
player_data_frame.propagate(0)

# Campo de entrada de dados
# texto lateral usando grid com posicionamento de colunas e linhas
Label(player_data_frame, text="Nº cartela: ").grid(row=0, ipady=5, padx=3, sticky=W)
Label(player_data_frame, text="Nome: ").grid(row=1, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Endereço: ").grid(row=2, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Data: ").grid(row=3, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Nº escolhidos: ").grid(row=4, padx=3,ipady=5, sticky=W)


# label de entrada
#bd = border, bg = background-color
card_number = Entry(player_data_frame).grid(row=0, column= 1)
player_name = Entry(player_data_frame).grid(row=1, column= 1)
adress_player = Entry(player_data_frame).grid(row=2, column= 1)
start_data = Entry(player_data_frame).grid(row=3, column=1)
number_choice_index1 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1, sticky=W, padx=5)
number_choice_index2 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1, sticky=E, padx=1)
number_choice_index3 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1)
number_choice_index4 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=4, sticky=W, padx=12)
number_choice_index5 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=5, sticky=W, padx=12)
number_choice_index6 = Entry(player_data_frame, width=3).grid(row=4, column=6, sticky=W, padx=12)
number_choice_index7 = Entry(player_data_frame, width=3).grid(row=4, column=7, sticky=W, padx=12)
number_choice_index8 = Entry(player_data_frame, width=3).grid(row=4, column=8, sticky=W, padx=12)
number_choice_index9 = Entry(player_data_frame, width=3).grid(row=4, column=9, sticky=W, padx=12)
number_choice_index10 = Entry(player_data_frame, width=3).grid(row=4, column=10, sticky=W, padx=12)

table_frame = Frame(windows_main)
table_frame.pack(side="right", fill="both")

commands_frame = Frame(windows_main)
commands_frame.pack(side="bottom", expand=True)

# mantém a janela aberta
=======
# Interface gráfica
# Importa a biblioteca do tkinter
from logging import root
from textwrap import fill
from tkinter import *
import tkinter
from tokenize import String
from turtle import left, width
from typing import Container
  
def limitar_tamanho(p):
    if len(p) > 2:
        return False
    return True

value = True
windows_main = tkinter.Tk(className="Inteface graphic - Bolão", )

vcmd = windows_main.register(func=limitar_tamanho)
  

# Insere o nome da janela
windows_main.title("Interface Bolão")

# Centralizando a screen
windows_main.resizable(False, False)  # Desativa o reajuste de tela padrão do windows

window_height = 800 # altura da janela
window_width = 1200 # largura da janela

screen_width = windows_main.winfo_screenwidth() # retorna a largura da tela
screen_height = windows_main.winfo_screenheight() # retorna a altura da tela

x_cordinate = int((screen_width/2) - (window_width/2)) # posição central
y_cordinate = int((screen_height/2) - (window_height/2)) # posição central

windows_main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) # Gerência o tamanho da tela

# cor de fundo
windows_main.configure(background="white")

# Frame de dados do usuário
player_data_frame = Frame(windows_main)
player_data_frame.pack(expand=True, side="left")
player_data_frame.propagate(0)

# Campo de entrada de dados
# texto lateral usando grid com posicionamento de colunas e linhas
Label(player_data_frame, text="Nº cartela: ").grid(row=0, ipady=5, padx=3, sticky=W)
Label(player_data_frame, text="Nome: ").grid(row=1, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Endereço: ").grid(row=2, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Data: ").grid(row=3, ipady=5, padx=3,sticky=W)
Label(player_data_frame, text="Nº escolhidos: ").grid(row=4, padx=3,ipady=5, sticky=W)


# label de entrada
#bd = border, bg = background-color
card_number = Entry(player_data_frame).grid(row=0, column= 1)
player_name = Entry(player_data_frame).grid(row=1, column= 1)
adress_player = Entry(player_data_frame).grid(row=2, column= 1)
start_data = Entry(player_data_frame).grid(row=3, column=1)
number_choice_index1 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1, sticky=W, padx=5)
number_choice_index2 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1, sticky=E, padx=1)
number_choice_index3 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=1)
number_choice_index4 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=4, sticky=W, padx=12)
number_choice_index5 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=5, sticky=W, padx=12)
number_choice_index6 = Entry(player_data_frame, width=3).grid(row=4, column=6, sticky=W, padx=12)
number_choice_index7 = Entry(player_data_frame, width=3).grid(row=4, column=7, sticky=W, padx=12)
number_choice_index8 = Entry(player_data_frame, width=3).grid(row=4, column=8, sticky=W, padx=12)
number_choice_index9 = Entry(player_data_frame, width=3).grid(row=4, column=9, sticky=W, padx=12)
number_choice_index10 = Entry(player_data_frame, width=3).grid(row=4, column=10, sticky=W, padx=12)

table_frame = Frame(windows_main)
table_frame.pack(side="right", fill="both")

commands_frame = Frame(windows_main)
commands_frame.pack(side="bottom", expand=True)

# mantém a janela aberta
>>>>>>> e45b9c5976ba6b89c14a8de58c7c9db4eb127864
windows_main.mainloop()