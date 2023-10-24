from tkinter import *

def graciasporjugar(nombre, tiempo, preguntas):
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
        devolucion_label.grid(row=3, column=0)
    elif preguntas >=12:
        devolucion_label = Label(ventana_gracias_jugar, text='Estas Promocionado, segui asi')
        devolucion_label.grid(row=3, column=0)
    elif preguntas >=10:
        devolucion_label = Label(ventana_gracias_jugar, text='Un glorioso cuatro!')
        devolucion_label.grid(row=3, column=0)
    else:
        devolucion_label = Label(ventana_gracias_jugar, text='Nos veremos en diciembre!')
        devolucion_label.grid(row=3, column=0)

    resultado_tiempo = Label(ventana_gracias_jugar, text=f'Y tu tiempo para responder fue de: {tiempo} segundos')
    resultado_tiempo.grid(row=4, column=0)

    boton_inicio = Button(ventana_gracias_jugar, text='Gracias Por Jugar')
    boton_inicio.grid(row=5, column=0)


    ventana_gracias_jugar.mainloop()