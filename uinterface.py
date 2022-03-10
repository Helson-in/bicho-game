# Interface gráfica
# Importa a biblioteca do tkinter
from logging import root
from textwrap import fill
from tkinter import *
import tkinter
from tokenize import String
from turtle import left, width
from typing import Container
from tkinter import ttk
  
# Função para inserir um objeto na tabela
def insert():
    if var_id.get() == "" or var_name.get() == "" or var_adress == "":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    tree_view.insert("", "end", values=(var_id.get(), var_name.get(), var_adress.get()))
    var_id.delete(0,END)
    var_name.delete(0,END)
    var_adress.delete(0,END)
    var_id.focus()
    
# Função para deletar um objeto da tabela
def delete():
    try:
        select_item = tree_view.selection()[0]
        tree_view.delete(select_item)    
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser deletado")
        
def catch():
    try:
        select_item = tree_view.selection()[0]
        values_person = tree_view.item(select_item, "values")
        print("ID: " + values_person[0])
        print("Nome: " + values_person[1])    
        print("Endereço: " + values_person[2])    
        print("Pontos: " + values_person[3])    
            
    except:
        messagebox.showinfo(title="ERRO", message="Selecione um elemento a ser exibido")

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

window_height = 700 # altura da janela
window_width = 800 # largura da janela

screen_width = windows_main.winfo_screenwidth() # retorna a largura da tela
screen_height = windows_main.winfo_screenheight() # retorna a altura da tela

x_cordinate = int((screen_width/2) - (window_width/2)) # posição central
y_cordinate = int((screen_height/2) - (window_height/2)) # posição central

windows_main.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) # Gerência o tamanho da tela

# cor de fundo
#windows_main.configure(background="black")

# Frame da tabela
table_frame = LabelFrame(windows_main, text="Tabela")
table_frame.pack(expand=True, ipadx=10, ipady=10)

# Criando a tabela de visualização // Treeview
tree_view = ttk.Treeview(table_frame, columns=('id','name','adress','score'), show='headings')
tree_view.column('id',minwidth=0, width=100)
tree_view.column('name',minwidth=0, width=200)
tree_view.column('adress',minwidth=0, width=200)
tree_view.column('score',minwidth=0, width=100)
tree_view.heading('id', text='ID')
tree_view.heading('name', text='NOME')
tree_view.heading('adress', text='ENDEREÇO')
tree_view.heading('score', text='PONTOS')

tree_view.pack(expand=True)

# Frame de dados do usuário
player_data_frame = LabelFrame(windows_main, text="Registro")
player_data_frame.pack(expand=True, ipadx="40")

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
number_choice_index6 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=6, sticky=W, padx=12)
number_choice_index7 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=7, sticky=W, padx=12)
number_choice_index8 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=8, sticky=W, padx=12)
number_choice_index9 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=9, sticky=W, padx=12)
number_choice_index10 = Entry(player_data_frame, width=3,validate='key', validatecommand=(vcmd, '%P')).grid(row=4, column=10, sticky=W, padx=12)

register_player_button = Button(player_data_frame, text="Registrar", width=8)
register_player_button.grid(row=5, columnspan=10, pady=10, ipadx=2, ipady=2)

# Frame de botões de comando
commands_frame = LabelFrame(windows_main, text="comandos", padx=130)

insert_button = Button(commands_frame, text="Insert", command=insert, width=50)
delete_button = Button(commands_frame, text="delete", command=delete, width=50)
catch_button = Button(commands_frame, text="catch", command=catch, width=50)

commands_frame.pack(expand=True, ipady=20)

insert_button.pack(expand=True, anchor='center')
delete_button.pack(expand=True, anchor='center')
catch_button.pack(expand=True, anchor='center')

# mantém a janela aberta
windows_main.mainloop()