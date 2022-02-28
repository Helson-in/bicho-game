from tkinter import *
from tkinter import ttk

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
