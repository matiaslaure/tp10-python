from tkinter import *


def elegir():
    pantalla.config(text="{}".format(seleccion.get()))


def reset():
    seleccion.set(None)
    pantalla.config(text="")

vent = Tk()

seleccion = StringVar()

seleccion.set(None)

titulo = Label(vent, text='Mi Progreso en python', bg='red', fg= 'white', padx= 20, pady= 20)
titulo.pack(fill= 'x')


Radiobutton(vent, text="Muy bien", variable = seleccion, value = 'MB', command = elegir).pack(anchor=W)
Radiobutton(vent, text="Bien", variable = seleccion, value = 'B', command = elegir).pack(anchor=W)
Radiobutton(vent, text="Regular", variable = seleccion, value = 'R', command = elegir).pack(anchor=W)
Radiobutton(vent, text = "Mal", variable = seleccion, value = 'M', command = elegir).pack(anchor=W)

pantalla = Label(vent)

pantalla.pack()

Button(vent, text="Reiniciar", command=reset).pack()

titulo = Label(vent, text='Gracias por evaluarme', bg='skyblue', fg= 'white', padx= 20, pady= 20)
titulo.pack(fill='x')



vent.mainloop()
