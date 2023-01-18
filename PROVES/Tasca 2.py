import random

#tasca 1
#demano el temps
'''temps=input("Indica el temps: ").split()
#divideixo els minuts entre 60 per a saber quantes hores son
hores=int(int(temps[2])/60)
print ("HORES1: ",hores)
#agafo el residu de de la divisió dels minuts entre 60.
minuts=int(int(temps[2])%60)
print ("MINUTS1: ",minuts)
#sumo les hores que indica l'usuari amb l'hora que es
hores += int(temps[0])
print ("HORES2: ",hores)
minuts += int(temps[1])
print ("MINUTS2: ",minuts)
#faig un bucle i agafo el residu en cas de que sigui més gran que 23 (les hores) o més gran que 59 (els minuts)
while True:
    if hores >23:
        hores=hores%24
        print ("HORES: ",hores)
    elif minuts > 59:
        minuts=minuts%60
        hores += 1
        print ("MINUTS: ",minuts)
    elif hores <=23 and minuts <= 59:
        break   

print("L'event acabarà a les:",str(hores)+":"+str(minuts))'''

'''#tasca 2
#no me dona temps a comentar més

secret_number = random.randrange(25)
print (secret_number)
numero_usuari = int(input("Introdueix un número enter: "))

while True:
    if secret_number == numero_usuari:
        print("El número del mag era:",secret_number)
        print("Ben fet, muggle! Ets lliure ara")
        break
    elif int(secret_number) != numero_usuari:
        print("Ha, ha! Estàs atrapat al meu bucle!")
        numero_usuari = int(input("Torna a introduir un número enter: "))'''

'''#tasca 3

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
llista_elementsunics=[]

for i in my_list:
    if my_list.count(i) == 1:
        llista_elementsunics.append(i)
        print ("APPEND",llista_elementsunics)
    elif i in llista_elementsunics:
        pass
    elif my_list.count(i) > 1:
        llista_elementsunics.append(i)
        print ("2",llista_elementsunics)
print(my_list)
print(llista_elementsunics)'''