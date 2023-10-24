import sqlite3
import tkinter as tk
from tkinter import messagebox
import random
import time
from pantallaFinJuego import findeljuego

conn = sqlite3.connect('jugadores.bd')
cursor = conn.cursor()

preguntas_utilizadas = []
contador_correctas = 0
contador_incorrectas = 0
contador_preguntas = 0

pregunta_actual = None

tiempo_total = 0

def juegopreguntas(nombre, ventana_menu_juego):
    global tiempo_total 
    ventana_menu_juego.destroy()
    def cargar_pregunta():
        global pregunta_actual, contador_preguntas
        
        if contador_preguntas < 15:
            # Filtra las preguntas que no se han utilizado
            preguntas_no_utilizadas = [pregunta for pregunta in preguntas if pregunta[0] not in preguntas_utilizadas]
            
            if preguntas_no_utilizadas:
                pregunta_actual = random.choice(preguntas_no_utilizadas)
                preguntas_utilizadas.append(pregunta_actual[0])

                opciones_pregunta = [pregunta_actual[2], pregunta_actual[3], pregunta_actual[4], pregunta_actual[5]]
                random.shuffle(opciones_pregunta)

                pregunta_label.config(text=pregunta_actual[1])
                opciones[0].config(text=opciones_pregunta[0])
                opciones[1].config(text=opciones_pregunta[1])
                opciones[2].config(text=opciones_pregunta[2])
                opciones[3].config(text=opciones_pregunta[3])
                contador_preguntas += 1
            else:
                messagebox.showinfo("Fin del juego", "Todas las preguntas han sido utilizadas.")
                detener_cronometro()
        else:
            messagebox.showinfo("Fin del juego", "Has completado 15 preguntas.")
            detener_cronometro()
            findeljuego(nombre, tiempo_transcurrido, contador_correctas)
            
    cursor.execute("SELECT * FROM preguntas")
    preguntas = cursor.fetchall()

    def verificar_respuesta(respuesta_elegida):
        global contador_correctas, contador_incorrectas, pregunta_actual

        if pregunta_actual is not None:
            if respuesta_elegida == pregunta_actual[2]:
                contador_correctas += 1
                contador_correctas_label.config(text=f"Respuestas Correctas: {contador_correctas}")
            else:
                contador_incorrectas += 1
                contador_incorrectas_label.config(text=f"Respuestas Incorrectas: {contador_incorrectas}")
            cargar_pregunta()
        else:
            messagebox.showinfo("Espera", "No hay pregunta disponible en este momento. Cargando una nueva pregunta...")
            cargar_pregunta()

    def iniciar_cronometro():
        global tiempo_inicial
        tiempo_inicial = time.time()
        actualizar_cronometro()

    def detener_cronometro():
        tiempo_transcurrido = int(time.time() - tiempo_inicial)
        tiempo_total_label.config(text=f"Tiempo total: {tiempo_total + tiempo_transcurrido} s")
        ventana.after_cancel(cronometro_id)

    def actualizar_cronometro():
        global tiempo_transcurrido 
        tiempo_transcurrido = int(time.time() - tiempo_inicial)
        tiempo_total_label.config(text=f"Tiempo total: {tiempo_total + tiempo_transcurrido} s")
        global cronometro_id
        cronometro_id = ventana.after(1000, actualizar_cronometro)  # Actualiza el cronómetro cada segundo (1000 ms)

    def reiniciar_juego():
        global contador_correctas, contador_incorrectas, tiempo_total
        contador_correctas = 0
        contador_incorrectas = 0
        tiempo_total = 0
        contador_correctas_label.config(text="Respuestas Correctas: 0")
        contador_incorrectas_label.config(text="Respuestas Incorrectas: 0")
        tiempo_total_label.config(text="Tiempo total: 0 s")
        preguntas_utilizadas.clear()
        cargar_pregunta()

    ventana = tk.Tk()
    ventana.title("Juego de Preguntas")
    pregunta_label = tk.Label(ventana, text="")
    pregunta_label.grid(row=0, column=0, columnspan=2)

    opciones = []
    for i in range(4):
        row = 1 if i < 2 else 2
        column = i if i < 2 else i - 2
        opciones.append(tk.Button(ventana, text="", command=lambda i=i: verificar_respuesta(opciones[i].cget("text"))))
        opciones[i].grid(row=row, column=column)

    contador_correctas_label = tk.Label(ventana, text="Respuestas Correctas: 0")
    contador_correctas_label.grid(row=5, column=0, columnspan=2)

    contador_incorrectas_label = tk.Label(ventana, text="Respuestas Incorrectas: 0")
    contador_incorrectas_label.grid(row=6, column=0, columnspan=2)

    tiempo_total_label = tk.Label(ventana, text="Tiempo total: 0 s")
    tiempo_total_label.grid(row=7, column=0, columnspan=2)

    reiniciar_button = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
    reiniciar_button.grid(row=8, column=0, columnspan=2)

    iniciar_cronometro()  
    cargar_pregunta()

    ventana.mainloop()
    conn.close()
