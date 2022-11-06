#Juego del trivial
#Variables
 
#Menu de opciones
print ("Bienvenido a Trivial Pursuit")
print "Pon el numero el numero 1 y empieza el juego!"
print "1 - Historia"
print "2 - Geografia"
print "3 - Deportes"
print "4 - Matematicas"
print "5 - Ingles"
print "6 - Ciencias Naturales"
print "7 - Harry potter"
print "8 - Cine"
print "9 - Series"
print "10 - Informatica"
print "11 - Fisica"
print "12 - Musicos importantes"
print "13 - Gramatica"
print "14 - Capitales"
 
opcion = int (input())
puntos = 0
#Pregunta de Historia
print "Pregunta de Historia"
print "Cual es el Descubridor de America?"
nombre = raw_input()
if nombre == "Cristobal":
	print "Efectivamente, lo has acertado"
	puntos = puntos + 1
else:
	print "Muah,Muah,Muah...Estudia historia"
print "Quien fue el primer rey borbon?"
nombre = raw_input()
if nombre == "Felipe V":
	print "Efectivamente lo has acertado"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah...Atiende en clase de historia"
	puntos = puntos - 1
#Pregunta de Geografia			
print "pregunta de Geografia"	
print "Donde esta Transilvania?"
nombre = raw_input()
if nombre == "En Rumania":
	print "Muy bien"
	puntos = puntos + 1
else:	
	print "Muah,Muah,Muah...Estudiate el mapa fisico de europa"
print "Que Rio pasa por Paris?"
nombre = raw_input()
if nombre == "El Sena":
	print "Muy bien se nota que te estudias el atlas"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah...estudia"
	puntos = puntos -1
#Pregunta de Deportes			
print "Pregunta de Deportes"
print "Donde se celebro el mundial de 2006?"
nombre = raw_input()
if nombre == "En Alemania":
	print "Se nota que te gusta el futbol"
	puntos = puntos + 1
else:		
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Quien es el maximo goleador del Mundial de 2010?"
nombre = raw_input()
if nombre == "Villa":
	print "Se nota que has visto este anho del mundial"	
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
#Pregunta de Matematicas
print "Pregunta de Matematicas"
print "Cual es la raiz cuadrada de 100?"
nombre = raw_input()
if nombre == "10":
	print "Se nota que atiendes en clase"		
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Quien fue una de las	personas mas importantes de las matematicas de Espania?"	 
nombre = raw_input()
if nombre == "Torres Quevedo":
	print "Se nota que te gustan las matematicas"
	puntos = puntos + 1 
else:
	print "Muah, Muah, Muah...Atiende en clase"
	puntos = puntos - 1
#Pregunta de Ingles
print "Pregunta de Ingles" 
print "Cual es el pasado del verbo coger?"
nombre = raw_input()
if nombre == "Caught":
	print "Te gusta el ingles verdad?"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah...Estudiate los verbos irregulares"	
	puntos = puntos -1
print "Que significa must?"
nombre = raw_input()
if nombre == "Deber":
	print "Muy bien"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah...Comprate un diccionario de ingles"
	puntos = puntos - 1
#Pregunta de Ciencias Naturales	
print "Pregunta de Ciencias Naturales"
print "Cual es el arbol mas grande del mundo?"
nombre = raw_input()
if nombre == "El Secuoya":
	print "Muy bien se nota que atiendes en clase"
	puntos = puntos - 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Dime el nombre de la parte de la planta que esta bajo tierra"
nombre = raw_input()
if nombre == "Raiz":
	print "Muy bien"	
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
#Pregunta de Harry Potter
print "Pregunta de Harry Potter"
print "Que significa la J y la K de J.K.rowling?"
nombre = raw_input()
if nombre == "Joanne y Kathleen":
	print "Te gusta Harry Potter verdad?"
	puntos = puntos +1
else:
	print"Muah, Muah, Muah...Se nota que no te gusta Harry Potter"
	puntos = puntos - 1
print "Cuales son las 3 maldiciones inperdonables y a que se castiga si son utilizadas contra personas?"
nombre = raw_input()
if "Imperius, Cruciatus y Avada Kedabra y se condenan con el ingreso en Azkaban":
	print "Se nota que te gustan los hechizos de Harry Potter"
	puntos = puntos - 1
else:
	print "Muah, Muah, Muah...Se nota que no te interesa Harry Potter"
	puntos = puntos - 1	
#Pregunta de Cine
print "Pregunta de Cine"
print "En que mes y anio han sacado Harry Potter y las Reliquias de la Muerte parte 1?"
nombre = raw_input()
if nombre == "En Noviembre de 2010":
	print "Muy bien"
	puntos = puntos + 1
else: 
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Como se llama el actor principal de la pelicula Karate Kid"
nombre = raw_input()
if nombre == "Jaden Smith":
	print "Muy bien"
	puntos = puntos -1
else:
	print "Muah, Muah, Muah... se nota que no te gusta el cine"
	puntos = puntos - 1
#Pregunta de Series 
print "Pregunta de Series"
print "Como se llama la serie en la que los muniecos son amarillos?"
nombre = raw_input()
if nombre == "Los Simpsons":
	print "Muy bien"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Como se llama la serie en la que la protagonista es selena gomez?"
nombre = raw_input()
if nombre == "Loa magos de weverly place":
	print "Se nota que ves Disney Channel"
	puntos = puntos + 1 
else:
	print "Muah, Muah, Muah...Se nota que no ves Disney Channel" 	
	puntos = puntos - 1
#Pregunta de Informatica
print "Pregunta de Informatica"
print "Que programa de programacion el icono es un gato?"
nombre = raw_input()
if nombre == "Scratch":
	print "Se nota que has ido al campus de sofware libre de 2010"
	puntos = puntos + 1
else:
	print"Muah, Muah, Muah...Se nota que no te interesa la informatica"
	puntos = puntos - 1
print "Que animal es el que representa a guadalinex?"
nombre = raw_input()
if nombre == "Un pinguino":
	print "Muy bien"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	punto = puntos - 1	
#Pregunta de Fisica
print "Pregunta de Fisica"
print "Una persona importante en el mundo de Fisica"
nombre = raw_input()
if nombre == "Eistein":
	print "Muy bien se nota que te gusta la  Fisica"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Cuantos generos de palanca hay?"
nombre = raw_input()
if nombre == "3":
	print "Muy Bien"
	puntos = puntos + 1
else:
	print "Muah, Muah, Muah..."	
	puntos = puntos - 1
#Preguntas de Musicos Importantes
print "Pregunta de Musicos importantes"
print "Que musico se quedo ciego"
nombre = raw_input()
if nombre == "Beethoven":
	print "Muy bien, se nota que te gusta la musica"
	puntos = puntos +1
else:	
	print "Muah, Muah, Muah...Atiende en clase"
	puntos = puntos - 1
print "Cual es el nombre de Beethoven"
nombre = raw_input()
if nombre == "Ludwing Van":
	print "Muy bien"
	puntos = puntos +1
else:
	print "Muah, Muah, Muah..."	
	puntos = puntos - 1
#Preguntas de Gramatica"	
print "Preguntas de Gramatica"
print "Que palabra es la"
nombre = raw_input()
if nombre == "Un Articulo":
	print "Muy bien lo has acertado"
	puntos = puntos +1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Que tipo de palabra es de"
nombre = raw_input()
if nombre == "Una Preposicion":
	print "Muy bien se no ta que te gusta la lengua"
	puntos = puntos +1
else:
	print "Muah, Muah, Muah...Atiende en clase de lengua"
	puntos = puntos - 1
#Preguntas de Capitales
print "Preguntas de Capitales"
print "Cual es la capital de Alemania"
nombre = raw_input()
if nombre == "Berlin":
	print "Muy bien"
	puntos = puntos +1
else:
	print "Muah, Muah, Muah..."
	puntos = puntos - 1
print "Cual es la capital de Islandia?"
nombre = raw_input()
if nombre == "Reiquiavik":
	print "Muy bien"
	puntos = puntos +1
else:
	print "Muah, Muah, Muah..."	
	puntos = puntos - 1
 
print "Los puntos son",puntos