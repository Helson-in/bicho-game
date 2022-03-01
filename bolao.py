from tkinter import *
from tkinter import ttk
<<<<<<< HEAD
import banco
import banco2
from numpy import insert

app = Tk()
app.title("Bolão System")
app.geometry("500x200")
app.configure(background="#dde")

listaNomes = [["001", "Alysson", "Centro", "0"], [
    "002", "Jordao", "Centro", "0"], ["003", "Eliane", "Centro", "0"]]

# Defindo a TreeView - colunas e o que mostrar
tv = ttk.Treeview(app, columns=(
    "ID", "nome", "endereço", "pontos"), show="headings")
# Definir colunas - Nome, Largura minima, Largura
tv.column("ID", minwidth=10, width=50)
tv.column("nome", minwidth=10, width=250)
tv.column("endereço", minwidth=10, width=100)
tv.column("pontos", minwidth=10, width=100)
tv.heading("ID", text="ID")
tv.heading("nome", text="Nome")
tv.heading("endereço", text="Endereço")
tv.heading("pontos", text="Pontos")
tv.pack()


# tv.insert("","end",values=(id,nome,endereço,pontos))

# Para executar o programa
app.mainloop()
=======

windows_main = Tk()
windows_main.title("Bolão System")
windows_main.geometry("800x600")

listaNomes = [["001", "Alysson", "Centro"], [
    "002", "Jordao", "Centro"], ["003", "Eliane", "Centro"]]

# Defindo a TreeView - colunas e o que mostrar
tv = ttk.Treeview(windows_main, columns=(
    "ID", "nome", "endereço"), show="headings")
# Definir colunas - Nome, Largura minima, Largura
tv.column("ID", minwidth=0, width=50)
tv.column("nome", minwidth=0, width=250)
tv.column("endereço", minwidth=0, width=100)
tv.heading("ID", text="ID")
tv.heading("nome", text="Nome")
tv.heading("endereço", text="Endereço")
tv.pack()

for (i, n, f) in listaNomes:
    tv.insert("", "end", values=(i, n, f))

windows_main.mainloop()
>>>>>>> e45b9c5976ba6b89c14a8de58c7c9db4eb127864
