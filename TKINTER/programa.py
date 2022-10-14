
from functools import partial
from sqlite3 import Row
from tkinter import *
import tkinter
from turtle import onclick, title

root = Tk()


def onclik(texto):
     acumulador["text"] = int(acumulador['texto']) + int(entrada.get()

# tamanho da janela a posiçao
root.geometry("220x300")

container_frame=tkinter.Frame(background="red", width=100, height=120)
container_frame.pack()


root.title("meu programa")
acumulador=Label(root, text="0")
entrada.grid(row=0, columm=0,columnspan=2)



entrada=Entry(root)
entrada.grid(row=2, columm=0)


botao=Button(root, text="acumulador", command=onclick)
botao.entrada.grid(row=2, columm=0)



root.mainloop()
