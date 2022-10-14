from tkinter import *
import tkinter.ttk as ttk

#f = 9*c/5 +32
#c = (f -32) * 5/9

def ToCelsius():
    result = float(input1.get())
    result = (result -32) * 5/9
    #txtResult["text"] = result + "ºC"
    convertido.set(str(result) + "ºC")

def ToFarenheith():
    result = float(input1.get())
    result = 9*result/5 + 32
    #txtResult["text"] = result + "ºF"
    convertido.set(str(result) + "ºF")

#UI
root = Tk()
root.geometry("400x400")
root.resizable(0,0)

#States
convertido = StringVar()

#Styles
style = ttk.Style()
style.configure("Txt.TLabel", foreground="#FFF", background="#555555",
                padding=10, font="Arial 14 bold")
style.configure("Btn.TButton", font="Arial 14", padding=10)
style.configure("Input.TEntry", font="Arial 14", padding=10)

#Widget
txtInfo = ttk.Label(root, text="Informe o valor a ser convertido", style="Txt.TLabel")
input1 = ttk.Entry(root, style="Input.TEntry")
txtResult = ttk.Label(root, style="Txt.TLabel", textvariable=convertido)
btnCelsius = ttk.Button(root, text="To Celsius", style="Btn.TButton", command=ToCelsius)
btnFarenheith = ttk.Button(root, text="To Fortinite", style="Btn.TButton", command=ToFarenheith)

#Packs
txtInfo.pack()
input1.pack()
txtResult.pack()
btnCelsius.pack()
btnFarenheith.pack()

root.mainloop()