from tkinter import *
from funciones import *
from PIL import Image, ImageTk 
import sqlite3
from tkinter import ttk
from tkinter import messagebox


base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

def comenzar_juego():
    nombre = nombre_jugador_entry.get()
    red_social = redsocial_jugador_entry.get()
    telefono = telefono_jugador_entry.get()
    try:
        cursor.execute('INSERT INTO jugadores (nombre, redSocial, telefono) VALUES (?,?,?)',
                   (nombre, red_social, telefono))
    except:
        messagebox.showinfo('Error','Tienes que agregar un Nombre.')

ventana_menu_juego = Tk()
ventana_menu_juego.title('Preguntados ISAUI')
ventana_menu_juego.resizable(height=500, width=500)

barra_menu = Menu(ventana_menu_juego)

ventana_menu_juego.config(menu=barra_menu)

barra_menu.add_command(label="Configuracion Preguntas", command=ejecutar_menu_preguntas)
barra_menu.add_command(label='Ayuda', command=lambda:instrucciones(ventana_menu_juego))

titulo_juego_label = Label(ventana_menu_juego, text='Preguntados ISAUI') 
titulo_juego_label.grid(row=0, column=0)

imagen = Image.open('logo_isaui.jpg')  
imagen = imagen.resize((300, 300))  
photo = ImageTk.PhotoImage(imagen)

label_imagen = Label(ventana_menu_juego, image=photo)
label_imagen.grid(row=1, column=0, padx=10, pady=10)

nombre_jugador_label = Label(ventana_menu_juego, text='Ingresa tu Nombre')
nombre_jugador_label.grid(row=2, column=0, columnspan=2)

nombre_jugador_entry = Entry(ventana_menu_juego)
nombre_jugador_entry.grid(row=3, column=0, columnspan=2)

redsocial_jugador_label = Label(ventana_menu_juego, text='Ingresa tu Instagram')
redsocial_jugador_label.grid(row=4, column=0, columnspan=2)

redsocial_jugador_entry = Entry(ventana_menu_juego)
redsocial_jugador_entry.grid(row=5, column=0, columnspan=2)

telefono_jugador_label = Label(ventana_menu_juego, text='Ingresa tu Numero de Telefono')
telefono_jugador_label.grid(row=6, column=0, columnspan=2)

telefono_jugador_entry = Entry(ventana_menu_juego)
telefono_jugador_entry.grid(row=7, column=0, columnspan=2)

text_label = Label(ventana_menu_juego, text='Estas Listo?')
text_label.grid(row=8, column=0, padx=5, pady=5, columnspan=2)

boton_comienzo_juego = Button(ventana_menu_juego, text='Comenzar Juego', command=comenzar_juego)
boton_comienzo_juego.grid(row=9, column=0, padx=5, pady=5, columnspan=2)

jugadores_label = Label(ventana_menu_juego, text='Jugadores')
jugadores_label.grid(row=0, column=1)

cursor.execute('''
    SELECT * FROM jugadores
    ORDER BY puntaje DESC;
''')

jugadores = cursor.fetchall()

jugadores_treeview = ttk.Treeview(ventana_menu_juego, columns=("Nombre", "Puntaje"))
jugadores_treeview.column("#0", width=0, stretch=NO)
jugadores_treeview.heading("#1", text='Nombre',anchor=CENTER) 
jugadores_treeview.heading("#2", text="Puntaje", anchor=CENTER)  # Centrar el encabezado 'Nombre'

for i in range(1,2):  
    jugadores_treeview.column(f"#{i}", anchor=CENTER)

for resultado in jugadores:
    nombre, puntaje = resultado

    jugadores_treeview.insert('','end', values=[nombre, puntaje])
                
jugadores_treeview.grid(row=1, column=1, padx=5, pady=5)

ventana_menu_juego.mainloop()