import subprocess
from tkinter import *

def ejecutar_menu_preguntas():
    script = 'menuPreguntas.py'
    subprocess.Popen(['python3', script])

def ejecutar_menu():
    script = 'menuinicio.py'
    subprocess.Popen(['python3', script])

def ejecutar_perfil():
    script = 'menuJugadores.py'
    subprocess.Popen(['python3', script])