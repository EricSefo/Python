#Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.

a = input("Dis-me un número de 4 dígits: ")
numero = int(a[0])+int(a[1])+int(a[2])+int(a[3])
print ("El resultat de la suma dels números és " + str(numero)+".")

#Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un programa que a partir d'una frase donada per l'usuari calculi:
#Número de caràcters.
frase = input("Dis-me una frase: ")
print("El número de caràcters escrits són: " + str(len(frase))+".")
#Número de paraules.
frase = input("Dis-me una frase: ")
print("El número de paraules escrites són: " + str(len(frase.split())))

#Frase amb totes les paraules en majúscula.
frase = input("Dis-me una frase: ")
print("Aquesta és la frase que has introduït per amb tots els caràcters en majúscula: " + str(frase.upper()))

#Frase  amb totes les paraules en minúscula.
frase = input("Dis-me una frase: ")
print("Aquesta és la frase que has introduït per amb tots els caràcters en minúscula: " + str(frase.lower()))

#Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència trobada a la frase.
frase = input("Dis-me una frase: ")
caracter = input("Quin caràcter vols buscar a la frase? ")
print("Aquesta és la posició del primer caràcter que has buscat: " + str(frase.find(caracter)))

#Preguntat un caràcter a l'usuari retorni la posició de la darrera coincidència trobada a la frase.
frase = input("Dis-me una frase: ")
caracter = input("Quin caràcter vols buscar a la frase? ")
print("Aquesta és la posició de l'últim caràcter que has buscat: " + str(frase.rfind(caracter)))

#Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a la frase.
frase = input("Dis-me una frase: ")
caracter = input("Quin caràcter vols buscar a la frase? ")
print("Aquesta és el número de coincidències trobades a la frase del caràcter escollit: " + str(frase.count(caracter)))

#Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).
frase = input("Dis-me una frase: ")
print("Aquesta és el número de vocals a la frase: " + str(frase.count("a")+frase.count("e")+frase.count("i")+frase.count("o")+frase.count("u")))

#Modifica el primer programa per a que abans de donar el resultat mostri si és cert que la cadena només conté números.
a = input("Dis-me un número de 4 dígits: ")
print("Verifiquem si el resultat té una cadena de números: " + str(a.isnumeric()))
