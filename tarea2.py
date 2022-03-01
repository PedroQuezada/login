from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Entry, Label

root=Tk()
root.title('Login')
root.geometry('400x200')
root.resizable(width=False, height=False)
root.config(bg="pink")

usuario=Label(root, text="ingrese nombre de Usuario:")
usuario.pack()

usuario1=StringVar()
usu=Entry(root, width=30, textvariable=usuario1)
usu.pack()

contraseña=Label(root,text='contraseña:')
contraseña.pack()

contra=StringVar()
contra1=Entry(root, width=30, textvariable=contra, show='*')
contra1.pack()

def ingresar():
    if usuario1.get()=="programador" and contra.get()=="123456":
        root.title("corrector")
    else:
        root.title("Incorrecto")

bt=Button(root, text="Entrar", command=ingresar)
bt.pack(side=BOTTOM)

root.mainloop()