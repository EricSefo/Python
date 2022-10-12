#Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi la suma dels números que la formen. 
#Heu d'utilitzar una funció interna per a fer la suma.
from numpy import append


cadena=input("Introdueix 4 caràcters númerics: ")

try:
    cadena_valors=[int(cadena[0]),int(cadena[1]),int(cadena[2]),int(cadena[3])]
    resultat=sum(cadena_valors)
    print ("La suma del números que forma la llista és de: "+str(resultat))
except ValueError:
    print ("Introdueix caràcters númerics!")
    
# Demana a l'usuari un número i afegeix-lo al final de la llista
# amb un mètode de llista.
cadena2=int(input("Introdueix 1 caràcter númerics més: "))
cadena_valors.append(cadena2)
try:
    print (cadena_valors)
except ValueError:
    print ("Introdueix caràcters númerics!")
    
#Ara elimina aquest número de la llista amb un mètode de llista.
try:
    del cadena_valors[4]
    print (cadena_valors)
except:
    print ("No hi ha cap valor a eliminar en la posició 4.")
    
#Ordena la llista amb un mètode de llista.
cadena_valors.sort()
print (cadena_valors)

#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.

