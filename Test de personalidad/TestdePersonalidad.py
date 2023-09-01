# hacer una pregunta al candidato  

tiempo = input( "1. ¿Prefieres pasar tiempo solo/a o rodeado/a de gente?\n(A) Solo/a\n(B) Rodeado/a de gente\n")

# imprimir qué tiempo eligien

print(f"Elegiste {tiempo}")

if tiempo == "A":
    print( "Muy buena eleccion puedes leer un libro o salir!" )
elif tiempo == "B":
    print( "Parece divertido!" )
else:
    print("Debes escribir A o B, digamos que te gusta leer.")

# hacer una SEGUNDA pregunta al candidato
situacion = input( "¿Cómo te sientes en situaciones nuevas?\n(A) Nervioso/a e incómodo/a\n(B)Emocionado/a y curioso/a\nA")

if situacion == "A":
    print( "Trata de aprender algo nuevo cuando este solo" )
elif situacion =="B":
    print( "Genial que te sientas bien" )
else:
    print("Por favor escribe A o B")
    situacion = "A"

# hacer una TERCERA  pregunta al candidato
value = input( "¿Qué es más importante para ti?\n(A) El dinero\n(B) El amor\n" )
if value == "A":
    print( "Dinero es unos de lo grande placeres de la vida!" )
elif value =="B":
    print( "El Amor buena elecion espero no te defrauden!" )
else:
    print("Debes escirbir A o B")
    value = "A"

# hacer una Cuarta  pregunta al candidato
genero = input( "¿Cual es su genero de musica favorito?\n(A) Reggeaton\n(B) Salsa\n" )
if genero == "A":
    print( "te gusta el perreo salvaje por lo visto!" )
elif genero =="B":
    print( "Eres un gran bailador!" )
else:
    print("Debes escribir A o B")
    genero = "A"

# hacer una Quinta  pregunta al candidato
problemas = input( "¿Cómo te enfrentas a los problemas?\n(A) Pensando detenidamente y buscando soluciones racionales\n(B) Siguiendo tus instintos y emociones\n" )
if problemas== "A":
    print( "Te gusta tener el control!" )
elif problemas=="B":
    print( "Eres un gran emprendedor!" )
else:
    print("Debes escribir A o B")
    problemas= "A"

# hacer una Ultima pregunta al candidato
enfoque = input( "¿Cuál es tu enfoque principal en la vida?\n(A) Estabilidad y seguridad\n(B) Aventura y emociones\n" )
if enfoque == "A":
    print("Te gusta estar tranquilo")
elif enfoque == "B":
    print("Eres un gran Viajero !")

# imprime las eleciones del candidato
print( f"Primero Elegiste {tiempo}, Luego {situacion}, Luego {value}, Luego {genero}, Luego {problemas}, Luego {enfoque}.")

# crear algunas variables para Las puntuaciones 

Pensamiento_introvertido = 0
Pensamiento_extravertido = 0
sentimental_introvertido = 0
sensacion_extravertido = 0

# actualizar las variables de puntuación en función de la elección de la tiempo
if tiempo == "A":
    Pensamiento_introvertido = Pensamiento_introvertido + 2
    sensacion_extravertido = sensacion_extravertido + 2
    sentimental_introvertido = sentimental_introvertido + 2
else:
    Pensamiento_extravertido = Pensamiento_extravertido + 1
    sensacion_extravertido = sensacion_extravertido + 1

# ctualizar las variables de puntuación según la elección del situacion
if situacion == "A":
    Pensamiento_introvertido = Pensamiento_introvertido + 2
    sensacion_extravertido = sensacion_extravertido + 2
    Pensamiento_extravertido = Pensamiento_extravertido - 1
else:
    Pensamiento_introvertido = Pensamiento_introvertido - 1
    sentimental_introvertido = sentimental_introvertido + 2
    sensacion_extravertido = sensacion_extravertido + 1

# actualizar las variables de puntuación en función de la elección del valor
if value == "A":
    Pensamiento_introvertido = Pensamiento_introvertido - 1
    sentimental_introvertido = sentimental_introvertido + 1
else:
    Pensamiento_introvertido = Pensamiento_introvertido + 2
    Pensamiento_extravertido = Pensamiento_extravertido + 2
    sensacion_extravertido = sensacion_extravertido + 1

# actualizar las variables de puntuación en función de la elección de la genero musical
if genero == "A":
    Pensamiento_extravertido = Pensamiento_extravertido + 2
    Pensamiento_introvertido = Pensamiento_introvertido + 2
else:
    sentimental_introvertido = sentimental_introvertido + 1
    sensacion_extravertido = sensacion_extravertido + 2

# actualizar las variables de puntuación en función de la elección de viaje
if problemas == "A":
    Pensamiento_introvertido = Pensamiento_introvertido - 2
    sentimental_introvertido = sentimental_introvertido + 1
    sensacion_extravertido = sensacion_extravertido - 1
else:
    Pensamiento_introvertido = Pensamiento_introvertido + 1
    Pensamiento_extravertido = Pensamiento_extravertido + 1
    sentimental_introvertido = sentimental_introvertido - 1

#  imprimir los resultados en función de la puntuación
if Pensamiento_introvertido >= 3:
    print( "Eres una persona que se interesa en las ideas y en la realidad interior,presta poca atención a las cosas externas" )
elif Pensamiento_extravertido >= 3:
    print( "Eres una persona que define sus ideas y pensamientos a traves de la realidad externa,eres una persona que le cuesta cambiar de opinion" )
elif sentimental_introvertido >= 3:
    print( "Eres una persona  ligeramente reservada aunque simpática y sociable con los amigos cercanos" ) 
else:
    print( "Eres una persona con un gran nivel de empatía y comprensión, facilidad para conectar y disfrutar de los demás" )