
from tkinter import *
from tkinter import ttk 


root = Tk()

root.geometry('400x400')
root.resizable(0, 0)

style = ttk.Style()
style.configure('Txt.TLabel', foreground="red", background='accccc',
                padding= 40,font='Arial 28', padding = 10)
style. configure('Btn.TButton', font='Arial 28', padding = 10)

text1 = ttk.Label(root, text='Texto', style='Txt.TLabel')
btnl1 = ttk.Button(root, text='Click me', style='Btn.TButton')

text1.pack()
btnl1.pack()

root.mainloop()
