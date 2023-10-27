import sqlite3
from tkinter import *
from tkinter import ttk

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

cursor.execute('''
    SELECT * FROM jugadores
    ORDER BY puntaje DESC;
''')

jugadores = cursor.fetchall()

ventana_jugadores = Tk()
ventana_jugadores.title('Perfil Jugadores')
ventana_jugadores.resizable(height=False, width=False)

jugadores_label = ttk.Label(ventana_jugadores, text='Perfil Jugadores',font= ("Gill Sans MT", 20,))
jugadores_label.grid(row=0, column=0)

jugadores_treeview = ttk.Treeview(ventana_jugadores, columns=("Nombre", "Puntaje","Tiempo","Red Social","Telefono"))
jugadores_treeview.column("#0", width=0, stretch=NO)
jugadores_treeview.heading("#1", text='Nombre',anchor=CENTER) 
jugadores_treeview.heading("#2", text="Puntaje", anchor=CENTER)  
jugadores_treeview.heading("#3", text="Tiempo", anchor=CENTER)
jugadores_treeview.heading("#4", text="Red Social", anchor=CENTER)
jugadores_treeview.heading("#5", text="Telefono", anchor=CENTER)   

for i in range(1,5):  
    jugadores_treeview.column(f"#{i}", anchor=CENTER)

for resultado in jugadores:
    id, nombre, redSocial, numero, puntaje, tiempo  = resultado

    jugadores_treeview.insert('','end', values=[nombre, puntaje, tiempo, redSocial, numero])

jugadores_treeview.grid(row=1, column=0, padx=5, pady=5)

ventana_jugadores.mainloop()