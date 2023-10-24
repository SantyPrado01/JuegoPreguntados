from tkinter import *
import sqlite3
from funciones import ejecutar_menu


def findeljuego(nombre, tiempo, preguntas):

    base_datos = sqlite3.connect('jugadores.bd')
    cursor = base_datos.cursor()

    def gracias_jugar():

        redSocial = red_social_entry.get()
        numero = numero_telefono_entry.get()
        puntaje = preguntas * 100
        cursor.execute('INSERT INTO jugadores (nombre, redSocial, telefono, puntaje, tiempo) VALUES (?,?,?,?,?)',
                        (nombre, redSocial, numero, puntaje, tiempo))
        
        ventana_gracias_jugar.destroy()
        ejecutar_menu()
  
    ventana_gracias_jugar = Tk()
    ventana_gracias_jugar.title('Gracias por jugar')

    agradecimineto_label = Label(ventana_gracias_jugar, text=f'Gracias {nombre} por jugar')
    agradecimineto_label.grid(row=0, column=0, columnspan=2)

    resultado_label = Label(ventana_gracias_jugar, text='Resultado de tu partida')
    resultado_label.grid(row=1, column=0, columnspan=2)
    
    resultado_preguntas = Label(ventana_gracias_jugar, text= f'De 15 preguntas respondiste {preguntas}')
    resultado_preguntas.grid(row=2, column=0)

    if preguntas >= 15:
        devolucion_label = Label(ventana_gracias_jugar, text='Sos un genio, no tuviste ningun error!')
        devolucion_label.grid(row=3, column=0, columnspan=2)
    elif preguntas >=12:
        devolucion_label = Label(ventana_gracias_jugar, text='Estas Promocionado, segui asi')
        devolucion_label.grid(row=3, column=0, columnspan=2)
    elif preguntas >=10:
        devolucion_label = Label(ventana_gracias_jugar, text='Un glorioso cuatro!')
        devolucion_label.grid(row=3, column=0, columnspan=2)
    else:
        devolucion_label = Label(ventana_gracias_jugar, text='Nos veremos en diciembre!')
        devolucion_label.grid(row=3, column=0, columnspan=2)

    resultado_tiempo = Label(ventana_gracias_jugar, text=f'Y tu tiempo para responder fue de: {tiempo} segundos')
    resultado_tiempo.grid(row=4, column=0, columnspan=2)

    red_social_label = Label(ventana_gracias_jugar, text='Dejanos tu Instagram para contactarte! ')
    red_social_label.grid(row=5, column=0)

    red_social_entry = Entry(ventana_gracias_jugar)
    red_social_entry.grid(row=5, column=1)

    numero_telefono_label = Label(ventana_gracias_jugar, text='O dejanos tu numero')
    numero_telefono_label.grid(row=6, column=0)

    numero_telefono_entry = Entry(ventana_gracias_jugar)
    numero_telefono_entry.grid(row=6, column=1)

    boton_inicio = Button(ventana_gracias_jugar, text='Gracias Por Jugar', command=gracias_jugar)
    boton_inicio.grid(row=7, column=0, columnspan=2)


    ventana_gracias_jugar.mainloop()