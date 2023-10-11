import subprocess
from tkinter import *

def ejecutar_agregar_preguntas():
    script = 'agregarPreguntas.py'
    subprocess.Popen(['python3', script])

def ejecutar_menu_preguntas():
    script = 'menuPreguntas.py'
    subprocess.Popen(['python3', script])

def instrucciones(a):
    ventana_instrucciones = Toplevel(a)
    ventana_instrucciones.title('Instrucciones')
    