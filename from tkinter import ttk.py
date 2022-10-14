from tkinter import ttk
from tkinter import *
from tkinter.font import Font
# componente of widget (componentes)

janela = Tk()
janela.title("Minha primeira window")
janela.geometry("350x500")
janela.resizable(False,False)
Label (janela, text ="(1+2-3*4/5)            ",bg="gray", fg="white").pack(ipady=30)
Label(janela, text = "      " *50,bg="grey").pack()
def porcentual():
    print("calculando o porcentual")
Button(
    janela,
    text="%",
    relief=SOLID, 
    bg="orange",
    command=porcentual(),
    font=Font(family="Arial", size=18, weight="bold")
    ).pack()
Button(janela, text = "CE").pack()
Button(janela,text="c").pack()
Entry(janela).place(x=0, y=200)

janela.mainloop()

