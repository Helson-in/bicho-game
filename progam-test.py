<<<<<<< HEAD
#utilizando ancoragem nas label's
from tkinter import *
import os
import banco


def save_data():
    # validação de campo
    if textbox_name.get() != "":
        view_name = textbox_name.get()
        view_fone = textbox_fone.get()
        view_email = textbox_email.get()
        view_obs = textbox_obs.get("1.0", END)
        # comando de insert no banco de dados
        vquery= "INSERT INTO player_card (T_NAMECONTATCT, T_TELEFONECONTACT, T_EMAILCONTACT, T_OBS) VALUES ('"+view_name+"', '"+view_fone+"', '"+view_email+"', '"+view_obs+"')"
        banco.dml(vquery)
        
        # Reseta a variável
        textbox_name.delete(0, END)
        textbox_fone.delete(0, END)
        textbox_email.delete(0, END)
        textbox_obs.delete(1.0, END)
        print("Dados Gravados")
    else:
        print("ERROR")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(bg="#dde")


# Anchor positions: N=Norte, S=Sul, E=Leste, W=Oeste
#NE=Nordeste, SE=Sudeste, SO=Sudoeste, NO=Noroeste

####################### NOME

Label(app, text="Nome", bg="#dde", foreground="black", anchor=W).place(x=10, y=10, width=200, height=20)

textbox_name = Entry(app)
textbox_name.place(x=10, y=30, width=200, height=20)

####################### TELEFONE

Label(app, text="Telefone", bg="#dde", foreground="black", anchor=W).place(x=10, y=60, width=100, height=20)

textbox_fone = Entry(app)
textbox_fone.place(x=10, y=80, width=100, height=20)

###################### EMAil

Label(app, text="Email", bg="#dde", foreground="black", anchor=W).place(x=10, y=110, width=200, height=20)

textbox_email = Entry(app)
textbox_email.place(x=10, y=130, width=300, height=20)

###################### CAIXA DE ENTRADA

# componente de texto com mais de uma linha

Label(app, text="OBS:", bg="#dde", foreground="black", anchor=W).place(x=10, y=160, width=200, height=20)

textbox_obs = Text(app)
textbox_obs.place(x=10, y=180, width=300, height=80)

Button(app, text="Imprimir", command=save_data).place(x=10, y= 270, width=100, height=20)


app.mainloop()
=======
#utilizando ancoragem nas label's
from tkinter import *
import os
import banco


def save_data():
    # validação de campo
    if textbox_name.get() != "":
        view_name = textbox_name.get()
        view_fone = textbox_fone.get()
        view_email = textbox_email.get()
        view_obs = textbox_obs.get("1.0", END)
        # comando de insert no banco de dados
        vquery= "INSERT INTO player_card (T_NAMECONTATCT, T_TELEFONECONTACT, T_EMAILCONTACT, T_OBS) VALUES ('"+view_name+"', '"+view_fone+"', '"+view_email+"', '"+view_obs+"')"
        banco.dml(vquery)
        
        # Reseta a variável
        textbox_name.delete(0, END)
        textbox_fone.delete(0, END)
        textbox_email.delete(0, END)
        textbox_obs.delete(1.0, END)
        print("Dados Gravados")
    else:
        print("ERROR")

app=Tk()
app.title("CFB Cursos")
app.geometry("500x300")
app.configure(bg="#dde")


# Anchor positions: N=Norte, S=Sul, E=Leste, W=Oeste
#NE=Nordeste, SE=Sudeste, SO=Sudoeste, NO=Noroeste

####################### NOME

Label(app, text="Nome", bg="#dde", foreground="black", anchor=W).place(x=10, y=10, width=200, height=20)

textbox_name = Entry(app)
textbox_name.place(x=10, y=30, width=200, height=20)

####################### TELEFONE

Label(app, text="Telefone", bg="#dde", foreground="black", anchor=W).place(x=10, y=60, width=100, height=20)

textbox_fone = Entry(app)
textbox_fone.place(x=10, y=80, width=100, height=20)

###################### EMAil

Label(app, text="Email", bg="#dde", foreground="black", anchor=W).place(x=10, y=110, width=200, height=20)

textbox_email = Entry(app)
textbox_email.place(x=10, y=130, width=300, height=20)

###################### CAIXA DE ENTRADA

# componente de texto com mais de uma linha

Label(app, text="OBS:", bg="#dde", foreground="black", anchor=W).place(x=10, y=160, width=200, height=20)

textbox_obs = Text(app)
textbox_obs.place(x=10, y=180, width=300, height=80)

Button(app, text="Imprimir", command=save_data).place(x=10, y= 270, width=100, height=20)


app.mainloop()
>>>>>>> e45b9c5976ba6b89c14a8de58c7c9db4eb127864
