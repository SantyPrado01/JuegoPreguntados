import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

ventana_menu_preguntas = Tk()
ventana_menu_preguntas.title('Menu Preguntas')

menu_preguntas_label = Label(ventana_menu_preguntas, text='Menu Preguntas')
menu_preguntas_label.grid(row=0, column=0)

def tree_select(event):
    global datos
    item_seleccionado = tree.selection()
    fila_seleccionada = tree.item(item_seleccionado)
    datos = fila_seleccionada['values']

    pregunta_entry.delete(1.0, 'end')
    respuesta_correcta_entry.delete(1.0, 'end')
    respuesta_incorrecta_uno_entry.delete(1.0, 'end')
    respuesta_incorrecta_dos_entry.delete(1.0, 'end')
    respuesta_incorrecta_tres_entry.delete(1.0, 'end')

    pregunta_entry.insert(1.0, datos[1])
    respuesta_correcta_entry.insert(1.0, datos[2])
    respuesta_incorrecta_uno_entry.insert(1.0, datos[3])
    respuesta_incorrecta_dos_entry.insert(1.0, datos[4])
    respuesta_incorrecta_tres_entry.insert(1.0, datos[5])


base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

cursor.execute('SELECT * FROM preguntas')

preguntas = cursor.fetchall()

tree = ttk.Treeview(ventana_menu_preguntas, columns=("ID","Pregunta", "Respuesta Correcta", "Respuesta Incorrecta 1","Respuesta Incorrecta 2", "Respuesta Incorrecta 3"))
tree.bind("<<TreeviewSelect>>",tree_select)

tree.column("#0", width=0, stretch=NO)
tree.heading("#1", text='Numero de Pregunta',anchor=CENTER) 
tree.heading("#2", text='Pregunta',anchor=CENTER) 
tree.heading("#3", text="Respuesta Correcta", anchor=CENTER)
tree.heading("#4", text="Respuesta Incorrecta 1", anchor=CENTER)
tree.heading("#5", text="Respuesta Incorrecta 2", anchor=CENTER)
tree.heading("#6", text="Respuesta Incorrecta 3", anchor=CENTER)   
             
for i in range(1, 6):  
    tree.column(f"#{i}", anchor=CENTER)

for resultado in preguntas:
    id, pregunta, respuesta_correcta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres = resultado

    tree.insert('','end', values=[id, pregunta, respuesta_correcta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres])
                
tree.grid(row=8, column=0, padx=10, pady=10)

def agregar_pregunta():
    pregunta = pregunta_entry.get("1.0", 'end-1c')
    respuesta = respuesta_correcta_entry.get("1.0", 'end-1c')
    opcion_uno = respuesta_incorrecta_uno_entry.get("1.0", 'end-1c')
    opcion_dos = respuesta_incorrecta_dos_entry.get("1.0", 'end-1c')
    opcion_tres = respuesta_incorrecta_tres_entry.get("1.0", 'end-1c')

    cursor.execute('INSERT INTO preguntas (pregunta, respuesta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres) VALUES(?,?,?,?,?)',
        (pregunta, respuesta, opcion_uno, opcion_dos, opcion_tres)
    )
    base_datos.commit()

    messagebox.showinfo('Completado','La Pregunta ha sido agregada con éxito.')
    pregunta_entry.delete(1.0, 'end')
    respuesta_correcta_entry.delete(1.0, 'end')
    respuesta_incorrecta_uno_entry.delete(1.0, 'end')
    respuesta_incorrecta_dos_entry.delete(1.0, 'end')
    respuesta_incorrecta_tres_entry.delete(1.0, 'end')

def guardar_cambios():
    pregunta = pregunta_entry.get("1.0", 'end-1c')
    respuesta = respuesta_correcta_entry.get("1.0", 'end-1c')
    opcion_uno = respuesta_incorrecta_uno_entry.get("1.0", 'end-1c')
    opcion_dos = respuesta_incorrecta_dos_entry.get("1.0", 'end-1c')
    opcion_tres = respuesta_incorrecta_tres_entry.get("1.0", 'end-1c')

    cursor.execute('UPDATE preguntas SET pregunta=?, respuesta=?, respuesta_incorrecta_uno=?, respuesta_incorrecta_dos=?, respuesta_incorrecta_tres=? WHERE id_pregunta=?',
        (pregunta, respuesta, opcion_uno, opcion_dos, opcion_tres, datos[0])
    )
    base_datos.commit()

    messagebox.showinfo('Completado','La Pregunta ha sido modificada con éxito.')

def eliminar_pregunta():

        base_datos = sqlite3.connect('jugadores.bd')

        cursor = base_datos.cursor()

        cursor.execute("DELETE FROM preguntas WHERE id_pregunta=?", (datos[0],))

        base_datos.commit()

        base_datos.close()

        messagebox.showinfo('Completado','La pregunta ha sido eliminada con éxito.')


frame_formulario_preguntas = Frame(ventana_menu_preguntas)
frame_formulario_preguntas.grid(row=0, column=0, rowspan=4)

agregar_pregunta_label = Label(frame_formulario_preguntas, text='Agregar Preguntas')
agregar_pregunta_label.grid(row=1, column=0, columnspan=2)

pregunta_label = Label(frame_formulario_preguntas, text='Pregunta: ')
pregunta_label.grid(row=2, column=0)

pregunta_entry = Text(frame_formulario_preguntas, height=3, width=40)
pregunta_entry.grid(row=2, column=1)

respuesta_correcta_label = Label(frame_formulario_preguntas, text='Respuesta Correcta: ')
respuesta_correcta_label.grid(row=3, column=0)

respuesta_correcta_entry = Text(frame_formulario_preguntas, height=3, width=40)
respuesta_correcta_entry.grid(row=3, column=1)

respuesta_incorrecta_uno = Label(frame_formulario_preguntas, text='Opción 1: ')
respuesta_incorrecta_uno.grid(row=4, column=0)

respuesta_incorrecta_uno_entry = Text(frame_formulario_preguntas, height=2, width=40)
respuesta_incorrecta_uno_entry.grid(row=4, column=1)

respuesta_incorrecta_dos = Label(frame_formulario_preguntas, text='Opción 2: ')
respuesta_incorrecta_dos.grid(row=5, column=0)

respuesta_incorrecta_dos_entry = Text(frame_formulario_preguntas, height=3, width=40)
respuesta_incorrecta_dos_entry.grid(row=5, column=1)

respuesta_incorrecta_tres = Label(frame_formulario_preguntas, text='Opción 3: ')
respuesta_incorrecta_tres.grid(row=6, column=0)

respuesta_incorrecta_tres_entry = Text(frame_formulario_preguntas, height=3, width=40)
respuesta_incorrecta_tres_entry.grid(row=6, column=1)

boton_agregar_pregunta = Button(frame_formulario_preguntas, text='Agregar Pregunta', command=agregar_pregunta)
boton_agregar_pregunta.grid(row=7, column=0)

boton_modificar_pregunta = Button(frame_formulario_preguntas, text='Modificar Pregunta', command=guardar_cambios)
boton_modificar_pregunta.grid(row=7, column=1)

boton_eliminar_pregunta = Button(frame_formulario_preguntas, text='Eliminar Pregunta', command=eliminar_pregunta)
boton_eliminar_pregunta.grid(row=7, column=2)

ventana_menu_preguntas.mainloop()
