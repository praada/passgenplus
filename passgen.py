import random
import string
from tkinter import *
from tkinter import messagebox as MessageBox
import pyperclip

#def clases
def generar():
    longitud = 14
    caracteres = string.ascii_letters + string.punctuation + "1234567890"
    passwd = "".join(random.choice(caracteres) for _ in range(longitud))
    return passwd

def mostrar_password():
    passwd = generar()
    pyperclip.copy(passwd)
    MessageBox.showinfo("Copia tu password", f"Ya esta copiado tu password\n{passwd}")
#parte grafica
#ventana
ventana = Tk()
ventana.title("PassGen+")

#LOGO del PROGRAMA
imagen_link = PhotoImage(file="logo.png")
img_scale = 2
img_logo = imagen_link.subsample(img_scale)
Label(ventana, image=img_logo).grid(pady=5, row=0,column=0)

#colocar boton
boton = Button(ventana, text="Generar Password", command=mostrar_password, width=40)
boton.grid(padx=40,pady=10,row=2,column=0,columnspan=2)


ventana.mainloop()