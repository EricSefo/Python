#1. Crea un programa que demani números enters al usuari. Si l’usuari escriu 0, el programa es donarà 
# per finalitzat i informarà al usuari del número màxim entrat, el número mínim i de quants números s’han entrat.
'''n = []
t = 0
while True:
    try:
        f = int(input())
        if f == 0:
            break
        t += 1
        n.append(f)
    except:
        continue
if len(n) < 1:
    print("No has entrat cap número vàlid.")
else:
    print("Número màxim entrat:",max(n),"Número mínim entrat:",min(n),"Números entrats:",t)'''

#2. La successió de Finobacci es una successió on cada element es resultat de la suma dels dos anteriors. 
#De tal forma que: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, etc.
#Crea un algorisme que demani una entrada n, l’algorisme pintarà fins a n elements de la successió de Fibonacci. 
#Si n=2, el resultat serà 0, 1 si n=5 el resultat serà 0, 1, 1, 2, 3.

'''f = [0, 1]
n = int(input())
while True:
    if n in f:
        break
    f.append(f[-2] + f[-1])
print(f[:-1])'''

#3. Crea una funció que donada una entrada de l’usuari en forma de número enter natural X, 
# comprovi si aquest X és primer. Per fer-ho s’ha de comprovar que aquest X dividit per tots els nombres desde 2 fins a X-1 
# no donin una divisió amb resta igual a 0. Si passa la prova informa-ne al usuari. Si no indicar per quin nombre es divisible.

'''paco = int(input())
divisible = []
if paco == 0 or paco == 1:
    print("Aquest número no es considera un número prim ni compost:",paco)
    exit()
elif paco == 2:
    print("És un número prim")
    exit()
for i in range(2, paco):
    if i == paco-1:
        break
    elif (paco % i) == 0:
        divisible.append(i)
if len(divisible) == 0:
    print("És un número prim")
else:
    print("No és un número prim, aquests son els seus divisors:",divisible)'''

#4. Crea un programa que dona’t un número N comprovi tots els números que hi ha desde 2 
# fins a N i si son primers els guardi en un array que al acabar es mostri al usuaris. 
# Si N=8 es mostrarà per pantalla 2, 3, 5 i 7.

'''n = int(input())
primes = []
for i in range(2, n+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
print(primes)'''

#5. Crea un programa que vagi demanant entrades alfanumeriques al usuari, si aquestes entrades 
# contenen la lletra A guardarles en un array. Si l’usuari escriu “exit” acabar el programa i 
# mostrar les entrades que contenen la lletra A.

'''paca = []
while True:
    paco = input()
    if paco == "exit":
        break
    elif 'A' in paco: 
        paca.append(paco)
print("Les entrades que contenen la lletra A:",paca)'''

#6. Escriure un programa en python que demani un número natural X i que generi un diccionari on les 
# claus seràn desde el número 1 fins al número X i els valors siguin els cuadrats de les claus.

'''k = int(input())
if k < 0:
    exit()
dict = {}
for i in range(1, k+1):
    dict[i] = i**2
print(dict)'''

#7.Amplia l’exercici anterior per tal que el programa demani un segon número 
# Y (mès petit que el primer) i el programa consulti el valor de Y al diccionari creat anteriorment

'''X = int(input())
Y = int(input())
if X < 0 or Y < 0 or X <= Y:
    print("Els números entrats no són naturals o el segon valor introduït no és més petit que el primer.")
    exit()
d = {}
for i in range(1, X+1):
    d[i] = i**2
print("Valor de Y en el diccionari:",d[Y])'''