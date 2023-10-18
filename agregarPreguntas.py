import sqlite3
from tkinter import *
from tkinter import messagebox

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

def agregar_pregunta():
    pregunta = pregunta_entry.get()
    respuesta = respuesta_correcta_entry.get()
    opcion_uno = respuesta_incorrecta_uno_entry.get()
    opcion_dos = respuesta_incorrecta_dos_entry.get()
    opcion_tres = respuesta_incorrecta_tres_entry.get()

    cursor.execute('INSERT INTO preguntas (pregunta, respuesta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres) VALUES(?,?,?,?,?)',
        (pregunta, respuesta, opcion_uno, opcion_dos, opcion_tres)
    )
    base_datos.commit()

    messagebox.showinfo('Completado','La Pregunta a sido agregada con exito.')
    pregunta_entry.delete(0, 'end')
    respuesta_correcta_entry.delete(0, 'end')
    respuesta_incorrecta_uno_entry.delete(0, 'end')
    respuesta_incorrecta_dos_entry.delete(0, 'end')
    respuesta_incorrecta_tres_entry.delete(0, 'end')

ventana_agregar_preguntas = Tk()
ventana_agregar_preguntas.title('Agregar Preguntas')
ventana_agregar_preguntas.resizable(height=None, width=None)

agregar_pregunta_label = Label(ventana_agregar_preguntas, text='Agregar Preguntas')
agregar_pregunta_label.grid(row=0, column=0, columnspan=2)

pregunta_label = Label(ventana_agregar_preguntas, text='Pregunta: ')
pregunta_label.grid(row=2, column=0)

pregunta_entry = Entry(ventana_agregar_preguntas)
pregunta_entry.grid(row=2, column=1)

respuesta_correcta_label = Label(ventana_agregar_preguntas, text='Respuesta Correcta: ')
respuesta_correcta_label.grid(row=3, column=0)

respuesta_correcta_entry = Entry(ventana_agregar_preguntas)
respuesta_correcta_entry.grid(row=3, column=1)

respuesta_incorrecta_uno = Label(ventana_agregar_preguntas, text='Opcion 1: ')
respuesta_incorrecta_uno.grid(row=4, column=0)

respuesta_incorrecta_uno_entry = Entry(ventana_agregar_preguntas)
respuesta_incorrecta_uno_entry.grid(row=4, column=1)

respuesta_incorrecta_dos = Label(ventana_agregar_preguntas, text='Opcion 2: ')
respuesta_incorrecta_dos.grid(row=5, column=0)

respuesta_incorrecta_dos_entry = Entry(ventana_agregar_preguntas)
respuesta_incorrecta_dos_entry.grid(row=5, column=1)

respuesta_incorrecta_tres = Label(ventana_agregar_preguntas, text='Opcion 3: ')
respuesta_incorrecta_tres.grid(row=6, column=0)

respuesta_incorrecta_tres_entry = Entry(ventana_agregar_preguntas)
respuesta_incorrecta_tres_entry.grid(row=6, column=1)

boton_agregar_pregunta = Button(ventana_agregar_preguntas, text='Agregar', command=agregar_pregunta)
boton_agregar_pregunta.grid(row=7, column=0, columnspan=2)

ventana_agregar_preguntas.mainloop()