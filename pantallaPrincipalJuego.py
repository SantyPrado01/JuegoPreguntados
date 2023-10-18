import sqlite3
import tkinter as tk
from tkinter import messagebox
import random
import time

# Conecta a la base de datos
conn = sqlite3.connect('jugadores.bd')
cursor = conn.cursor()

# Crea una lista para llevar un registro de preguntas utilizadas
preguntas_utilizadas = []
contador_correctas = 0
contador_incorrectas = 0
contador_preguntas = 0
# Variable global para la pregunta actual
pregunta_actual = None

# Variable global para el tiempo total
tiempo_total = 0

# Función para cargar una pregunta aleatoria y mostrarla en la interfaz
def cargar_pregunta():
    global pregunta_actual, tiempo_inicial, contador_preguntas
    while contador_preguntas<15:
        cursor.execute("SELECT * FROM preguntas ORDER BY RANDOM() LIMIT 1")
        pregunta_actual = cursor.fetchone()
        if pregunta_actual[0] not in preguntas_utilizadas:
            break
    # Agrega la pregunta a la lista de preguntas utilizadas
    preguntas_utilizadas.append(pregunta_actual[0])

    opciones_pregunta = [pregunta_actual[2], pregunta_actual[3], pregunta_actual[4], pregunta_actual[5]]

    random.shuffle(opciones_pregunta)

    pregunta_label.config(text=pregunta_actual[1])
    opciones[0].config(text=opciones_pregunta[0])
    opciones[1].config(text=opciones_pregunta[1])
    opciones[2].config(text=opciones_pregunta[2])
    opciones[3].config(text=opciones_pregunta[3])

# Función para verificar la respuesta seleccionada
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

# Función para iniciar el cronómetro
def iniciar_cronometro():
    global tiempo_inicial
    tiempo_inicial = time.time()
    actualizar_cronometro()

# Función para detener el cronómetro
def detener_cronometro():
    tiempo_transcurrido = int(time.time() - tiempo_inicial)
    tiempo_total_label.config(text=f"Tiempo total: {tiempo_total + tiempo_transcurrido} s")
    ventana.after_cancel(cronometro_id)

# Función para actualizar el cronómetro
def actualizar_cronometro():
    tiempo_transcurrido = int(time.time() - tiempo_inicial)
    tiempo_total_label.config(text=f"Tiempo total: {tiempo_total + tiempo_transcurrido} s")
    global cronometro_id
    cronometro_id = ventana.after(1000, actualizar_cronometro)  # Actualiza el cronómetro cada segundo (1000 ms)

# Función para reiniciar el juego
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
pregunta_label.pack()

opciones = []
for i in range(4):
    opciones.append(tk.Button(ventana, text="", command=lambda i=i: verificar_respuesta(opciones[i].cget("text"))))
    opciones[i].pack()

contador_correctas_label = tk.Label(ventana, text="Respuestas Correctas: 0")
contador_correctas_label.pack()

contador_incorrectas_label = tk.Label(ventana, text="Respuestas Incorrectas: 0")
contador_incorrectas_label.pack()

tiempo_total_label = tk.Label(ventana, text="Tiempo total: 0 s")
tiempo_total_label.pack()

reiniciar_button = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
reiniciar_button.pack()

iniciar_cronometro()
cargar_pregunta()

ventana.mainloop()
conn.close()
