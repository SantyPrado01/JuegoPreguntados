import sqlite3
from tkinter import *
from tkinter import ttk
from funciones import *
from modificarPreguntas import *

ventana_menu_preguntas = Tk()
ventana_menu_preguntas.title('Menu Preguntas')

menu_preguntas_label = Label(ventana_menu_preguntas, text='Menu Preguntas')
menu_preguntas_label.grid(row=0, column=0)

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

cursor.execute('SELECT * FROM preguntas')

preguntas = cursor.fetchall()

tree = ttk.Treeview(ventana_menu_preguntas, columns=("Pregunta", "Respuesta Correcta", "Respuesta Incorrecta 1","Respuesta Incorrecta 2", "Respuesta Incorrecta 3"))
            
tree.column("#0", width=0, stretch=NO)
tree.heading("#1", text='Pregunta',anchor=CENTER) 
tree.heading("#2", text="Respuesta Correcta", anchor=CENTER)  # Centrar el encabezado 'Nombre'
tree.heading("#3", text="Respuesta Incorrecta 1", anchor=CENTER)  
tree.heading("#4", text="Respuesta Incorrecta 2", anchor=CENTER)
tree.heading("#5", text="Respuesta Incorrecta 3", anchor=CENTER)   
             
for i in range(1, 6):  
    tree.column(f"#{i}", anchor=CENTER)

for resultado in preguntas:
    id, pregunta, respuesta_correcta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres = resultado

    tree.insert('','end', values=[pregunta, respuesta_correcta, respuesta_incorrecta_uno, respuesta_incorrecta_dos, respuesta_incorrecta_tres])
                
tree.grid(row=1, column=0, padx=10, pady=10)

boton_agregar_pregunta = Button(ventana_menu_preguntas, text='Agregar Nueva Pregunta', command=ejecutar_agregar_preguntas)
boton_agregar_pregunta.grid(row=3, column=0)

boton_modificar_pregunta = Button(ventana_menu_preguntas, text='Modificar Pregunta', command=lambda:modificar_pregunta(tree, id))
boton_modificar_pregunta.grid(row=4, column=0)

ventana_menu_preguntas.mainloop()