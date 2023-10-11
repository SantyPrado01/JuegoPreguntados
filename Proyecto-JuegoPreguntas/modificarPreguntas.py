import sqlite3
from tkinter import *
from tkinter import messagebox

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

def modificar_pregunta(tree, id):

    item_seleccionado = tree.selection()
    if item_seleccionado:
        fila_seleccionada = tree.item(item_seleccionado)
        datos = fila_seleccionada['values']

        ventana_modificar_preguntas = Tk()
        ventana_modificar_preguntas.title('Modificar Preguntas')
        ventana_modificar_preguntas.resizable(height=None, width=None)

        agregar_pregunta_label = Label(ventana_modificar_preguntas, text='Modificar Preguntas')
        agregar_pregunta_label.grid(row=0, column=0, columnspan=2)

        pregunta_label = Label(ventana_modificar_preguntas, text='Pregunta: ')
        pregunta_label.grid(row=2, column=0)

        pregunta_entry = Entry(ventana_modificar_preguntas)
        pregunta_entry.grid(row=2, column=1)
        pregunta_entry.insert(0, datos[0])

        respuesta_correcta_label = Label(ventana_modificar_preguntas, text='Respuesta Correcta: ')
        respuesta_correcta_label.grid(row=3, column=0)

        respuesta_correcta_entry = Entry(ventana_modificar_preguntas)
        respuesta_correcta_entry.grid(row=3, column=1)
        respuesta_correcta_entry.insert(0, datos[1])

        respuesta_incorrecta_uno = Label(ventana_modificar_preguntas, text='Opcion 1: ')
        respuesta_incorrecta_uno.grid(row=4, column=0)

        respuesta_incorrecta_uno_entry = Entry(ventana_modificar_preguntas)
        respuesta_incorrecta_uno_entry.grid(row=4, column=1)
        respuesta_incorrecta_uno_entry.insert(0, datos[2])

        respuesta_incorrecta_dos = Label(ventana_modificar_preguntas, text='Opcion 2: ')
        respuesta_incorrecta_dos.grid(row=5, column=0)

        respuesta_incorrecta_dos_entry = Entry(ventana_modificar_preguntas)
        respuesta_incorrecta_dos_entry.grid(row=5, column=1)
        respuesta_incorrecta_dos_entry.insert(0, datos[3])

        respuesta_incorrecta_tres = Label(ventana_modificar_preguntas, text='Opcion 3: ')
        respuesta_incorrecta_tres.grid(row=6, column=0)

        respuesta_incorrecta_tres_entry = Entry(ventana_modificar_preguntas)
        respuesta_incorrecta_tres_entry.grid(row=6, column=1)
        respuesta_incorrecta_tres_entry.insert(0, datos[4])

        def guardar_cambios():
            pregunta = pregunta_entry.get()
            respuesta = respuesta_correcta_entry.get()
            opcion_uno = respuesta_incorrecta_uno_entry.get()
            opcion_dos = respuesta_incorrecta_dos_entry.get()
            opcion_tres = respuesta_incorrecta_tres_entry.get()

            cursor.execute('UPDATE preguntas SET pregunta=?, respuesta=?, respuesta_incorrecta_uno=?, respuesta_incorrecta_dos=?, respuesta_incorrecta_tres=? WHERE id_pregunta=?',
                (pregunta, respuesta, opcion_uno, opcion_dos, opcion_tres, id)
            )
            base_datos.commit()

            messagebox.showinfo('Completado','La Pregunta a sido modificada con exito.')
            ventana_modificar_preguntas.destroy()
            
        boton_modificar_pregunta = Button(ventana_modificar_preguntas, text='Modificar', command=guardar_cambios)
        boton_modificar_pregunta.grid(row=7, column=0, columnspan=2)

        ventana_modificar_preguntas.mainloop()



        