#Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi la suma dels números que la formen. 
#Heu d'utilitzar una funció interna per a fer la suma.

cadena=input("Introdueix 4 caràcters númerics: ")

try:
    cadena_valors=[int(cadena[0]),int(cadena[1]),int(cadena[2]),int(cadena[3])]
    resultat=sum(cadena_valors)
    print ("La suma del números que forma la llista és de: "+str(resultat))
except ValueError:
    print ("Introdueix caràcters númerics!")
    quit()
    
# Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.

try:
    cadena2=int(input("Introdueix 1 caràcter númerics més: "))
    cadena_valors.append(cadena2)
    print ("Aquesta és la llista actual amb el número nou: "+str(cadena_valors))
except ValueError:
    print ("Introdueix caràcters númerics!")
    quit()
    
#Ara elimina aquest número de la llista amb un mètode de llista.
del cadena_valors[4]
print ("Aquesta és la llista amb el número eliminat: "+str(cadena_valors))
    
#Ordena la llista amb un mètode de llista.
cadena_valors.sort()
print ("La llista ordenada ascendentment: "+str(cadena_valors))

#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.
maxim = max(cadena_valors)
minim = min(cadena_valors)
print ("El número màxim és: "+str(maxim)+" i el número mínim és: "+str(minim))

#Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().
suma = sum(cadena_valors)
length = len(cadena_valors)
resultat = suma / length
print ("Aquest és la mitjana aritmètica de la llista: "+str(resultat))