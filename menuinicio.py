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
ventana_menu_juego.iconbitmap('logo_preguntados.ico')
ventana_menu_juego.title('Preguntados ISAUI')
ventana_menu_juego.state('zoomed')
ventana_menu_juego.config(bg='white')
barra_menu = Menu(ventana_menu_juego)

##6EC1E4

ventana_menu_juego.config(menu=barra_menu)

barra_menu.add_command(label="Configuracion Preguntas", command=ejecutar_menu_preguntas)
barra_menu.add_command(label='Perfil Jugadores', command=ejecutar_perfil)

imagen = Image.open('preguntados.jpg')  
imagen = imagen.resize((1200, 250))  
photo_logo = ImageTk.PhotoImage(imagen)


frame = Frame(ventana_menu_juego)
frame.config(bg='white')
label_imagen = Label(frame, image=photo_logo, background='white')
label_imagen.grid(row=0, column=0, pady=60, columnspan=2)

nombre_jugador_label = ttk.Label(frame, text='Ingresa tu Nombre',font=('Roboto', 25),background='white', anchor="center", justify="center")
nombre_jugador_label.grid(row=2, column=0, padx=(10,50), pady=5, sticky="nsew")

nombre_jugador_entry = Entry(frame,font=('Roboto', 25))
nombre_jugador_entry.grid(row=3, column=0, padx=(10,50), pady=5)

text_label = ttk.Label(frame, text='Estas Listo?', font=('Roboto', 25),background='white', anchor="center", justify="center")
text_label.grid(row=4, column=0, padx=(10,50), pady=5, sticky="nsew")

boton_comienzo_juego = Button(frame, text='Comenzar Juego', command=comenzar_juego, font=('Robot',25), background='#0B4F64', fg='white')
boton_comienzo_juego.grid(row=5, column=0, padx=(10,50), pady=5)

jugadores_label = ttk.Label(frame, text='Jugadores', font=('Roboto', 25), background='white', anchor="center", justify="center")
jugadores_label.grid(row=1, column=1, padx=(50,10), pady=5, sticky="nsew")

frame.pack()

cursor.execute('''
    SELECT * FROM jugadores
    ORDER BY puntaje DESC;
''')

jugadores = cursor.fetchall()

fuente_cabecera = ('Roboto', 15)

style = ttk.Style()
style.configure("Treeview", rowheight=30)

jugadores_treeview = ttk.Treeview(frame, columns=("Nombre", "Puntaje","Tiempo"), style='Treeview')
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

jugadores_treeview.grid(row=2, column=1, pady=10, rowspan=4, sticky="nsew")


ventana_menu_juego.mainloop()
