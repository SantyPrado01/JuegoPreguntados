import sqlite3

base_datos = sqlite3.connect('jugadores.bd')
cursor = base_datos.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores(
    id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(255) NOT NULL,
    redSocial VARCHAR(255),
    telefono VARCHAR(255),
    puntaje FLOAT,
    tiempo FLOAT        
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS preguntas(
    id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta VARCHAR(255) NOT NULL,
    respuesta VARCHAR(255) NOT NULL,
    respuesta_incorrecta_uno VARCHAR(255) NOT NULL,
    respuesta_incorrecta_dos VARCHAR(255) NOT NULL,
    respuesta_incorrecta_tres VARCHAR(255) NOT NULL
    )
''')

