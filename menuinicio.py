from tkinter import *
from funciones import *
from PIL import Image, ImageTk 
from tkinter.font import Font
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from pantallaJuego import juegopreguntas

def comenzar_juego():
    nombre = nombre_jugador_entry.get()
    if nombre:
        juegopreguntas(nombre, ventana_menu_juego)
    else:
        messagebox.showerror('Error','Tienes que ingresar tu nombre')

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

ventana_menu_juego = Tk()
ventana_menu_juego.title('Preguntados ISAUI')
ventana_menu_juego.resizable(height=800, width=800)
ventana_menu_juego.config(bg='white')
barra_menu = Menu(ventana_menu_juego)

##6EC1E4

ventana_menu_juego.config(menu=barra_menu)

barra_menu.add_command(label="Configuracion Preguntas", command=ejecutar_menu_preguntas)
barra_menu.add_command(label='Configuracion Jugadores', command='perfilJugadores')

imagen = Image.open('logo.png')  
imagen = imagen.resize((400, 300))  
photo_logo = ImageTk.PhotoImage(imagen)

imagen_2 = Image.open('nombre.png')
imagen_2 = imagen.resize((1000,100))
photo_nombre = ImageTk.PhotoImage(imagen_2)

titulo_juego_label = Label(ventana_menu_juego, text='Preguntados ISAUI', font=('Arial', 40)) 
titulo_juego_label.grid(row=0, column=0, columnspan=3)

label_imagen = Label(ventana_menu_juego, image=photo_logo, background='white')
label_imagen.grid(row=1, column=0, padx=10, pady=10, rowspan=3)

nombre_jugador_label = Label(ventana_menu_juego, text='Ingresa tu Nombre',font=('Arial', 25))
nombre_jugador_label.grid(row=4, column=0, columnspan=2)

nombre_jugador_entry = Entry(ventana_menu_juego)
nombre_jugador_entry.grid(row=5, column=0, columnspan=2)

text_label = Label(ventana_menu_juego, text='Estas Listo?', font=('Arial', 25))
text_label.grid(row=6, column=0, padx=5, pady=5, columnspan=2)

boton_comienzo_juego = Button(ventana_menu_juego, text='Comenzar Juego', command=comenzar_juego, font=('Arial', 25))
boton_comienzo_juego.grid(row=7, column=0, padx=5, pady=5, columnspan=2)

jugadores_label = Label(ventana_menu_juego, text='Jugadores', font=('Arial', 20))
jugadores_label.grid(row=1, column=1, padx=5, pady=5)

cursor.execute('''
    SELECT * FROM jugadores
    ORDER BY puntaje DESC;
''')

jugadores = cursor.fetchall()

fuente_cabecera = ('Arial', 15)

style = ttk.Style()
style.configure("Treeview", rowheight=30)
style.configure('Custom.Treeview.heading', font=('Arial',35))

jugadores_treeview = ttk.Treeview(ventana_menu_juego, columns=("Nombre", "Puntaje","Tiempo"), style='Treeview')
jugadores_treeview.column("#0", width=0, stretch=NO)
jugadores_treeview.heading("#1", text='Nombre',anchor=CENTER) 
jugadores_treeview.heading("#2", text="Puntaje", anchor=CENTER)  
jugadores_treeview.heading("#3", text="Tiempo", anchor=CENTER) 

for i in range(1,3):  
    jugadores_treeview.column(f"#{i}", anchor=CENTER)

for resultado in jugadores:
    id, nombre, redSocial, numero, puntaje, tiempo  = resultado

    jugadores_treeview.insert('','end', values=[nombre, puntaje, tiempo], tags=("fuente_personalizada",))
    jugadores_treeview.tag_configure("fuente_personalizada", font=fuente_cabecera)

jugadores_treeview.grid(row=2, column=1, padx=5, pady=5)

ventana_menu_juego.mainloop()
