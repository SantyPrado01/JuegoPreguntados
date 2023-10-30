from tkinter import *
import sqlite3
from PIL import Image, ImageTk
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
        base_datos.commit()
        ejecutar_menu()
        ventana.destroy()
        
    ventana = Tk()
    ventana.iconbitmap('logo_preguntados.ico')
    ventana.state('zoomed')
    ventana.config(bg='white')
    ventana.title('Gracias por jugar')

    imagen = Image.open('isaui.png')  
    imagen = imagen.resize((600, 200))  
    photo_logo = ImageTk.PhotoImage(imagen)

    label_imagen = Label(ventana, image=photo_logo, background='white')
    label_imagen.pack(padx=15, pady=15)

    ventana_gracias_jugar = Frame(ventana)
    ventana_gracias_jugar.config(bg='white')
    agradecimineto_label = Label(ventana_gracias_jugar, text=f'Gracias {nombre} por jugar', font=('Roboto', 25), bg='white')
    agradecimineto_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    resultado_label = Label(ventana_gracias_jugar, text='Resultado de tu partida', font=('Roboto', 20), bg='white')
    resultado_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    resultado_preguntas = Label(ventana_gracias_jugar, text= f'De 15 preguntas respondiste {preguntas}', font=('Roboto', 20), bg='white')
    resultado_preguntas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    if preguntas >= 15:
        devolucion_label = Label(ventana_gracias_jugar, text='Sos un genio, no tuviste ningun error!', font=('Roboto', 20), bg='white')
        devolucion_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    elif preguntas >=12:
        devolucion_label = Label(ventana_gracias_jugar, text='Estas Promocionado, segui asi', font=('Roboto', 20), bg='white')
        devolucion_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    elif preguntas >=10:
        devolucion_label = Label(ventana_gracias_jugar, text='Un glorioso cuatro!', font=('Roboto', 20), bg='white')
        devolucion_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    else:
        devolucion_label = Label(ventana_gracias_jugar, text='Nos veremos en diciembre!', font=('Roboto', 20), bg='white')
        devolucion_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    resultado_tiempo = Label(ventana_gracias_jugar, text=f'Y tu tiempo para responder fue de: {tiempo} segundos', font=('Roboto', 20), bg='white')
    resultado_tiempo.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    red_social_label = Label(ventana_gracias_jugar, text='Dejanos tu Instagram para contactarte! ', font=('Roboto', 20), bg='white')
    red_social_label.grid(row=5, column=0, padx=10, pady=10)

    red_social_entry = Entry(ventana_gracias_jugar, font=('Roboto', 20))
    red_social_entry.grid(row=5, column=1, padx=10, pady=10)

    numero_telefono_label = Label(ventana_gracias_jugar, text='O dejanos tu numero: ', font=('Roboto', 20), bg='white')
    numero_telefono_label.grid(row=6, column=0, padx=10, pady=10)

    numero_telefono_entry = Entry(ventana_gracias_jugar, font=('Robot',20))
    numero_telefono_entry.grid(row=6, column=1, padx=10, pady=10)

    boton_inicio = Button(ventana_gracias_jugar, text='Gracias Por Jugar', command=gracias_jugar, font=('Robot',20), background='#0B4F64', fg='white')
    boton_inicio.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    ventana_gracias_jugar.pack()

    ventana.mainloop()