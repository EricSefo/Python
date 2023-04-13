#Crea una funció recursiva que rebi 
# com a parametres dos strings a i b, retorni si b es troba dintre de a (tindrem en compte majúscules i minúscules): 
#Pe:  esTroba("Un tete a tete con Tete", "te") = True

'''def esTroba(a,b):
    if a[:len(b)] == b:
        return True
    else:
        return esTroba(a[1:],b)
print(esTroba("Un tete a tete con Tete", "te"))'''

#Crea una funció recursiva que rebi com a parametres dos strings a i b, retorni una llista de posicions on b es troba dintre de a: 
#Pe:  posicions_de("Un tete a tete con Tete", "te") = [3, 5, 10, 12, 21]
'''def posicions_de(a,b,posicions=None,x=0):
    if posicions == None:
        posicions=[]
    if x+len(b) > len(a):
        return posicions
    if a[x:x+len(b)] == b:
        posicions.append(x)
    return posicions_de(a,b,posicions,x+1)
print(posicions_de("Un tete a tete con Tete", "te"))'''

#Crea un funció anomenada replicar que rebi una llista de números 
# i un parametre numèric natural i que generi una llista on es repliqui 
# tantes vegades com s’indica cada element. Pe: replicar([1,3,3,5], 2) = [1,1,3,3,3,3,5,5]
'''def replicar(llista, n):
    if not llista:  # Cas base: si la llista està buida, retornem una llista buida
        return []
    else:
        return [llista[0]]*n + replicar(llista[1:], n)
    
print(replicar([1,3,3,5], 2))'''

#Crea una funció recursiva que donat un array de número naturals en trobi el màxim. 
# Prohibit utilitzar funcions integrades del python!
'''maxim = int()
def max(x):
    global maxim
    if x[0] > maxim:
        maxim = x[0]
    if len(x) == 1:
        return maxim
    else:
        return max(x[1:])
print(max([4,43,23,26]))'''

#Crea una funció recursiva que donat un array de números i un número comprovi 
#si el número es troba dintre de la llista i retorni cert o fals.
#Pe: esTroba([1,2,3,4,5], 7) = false; esTroba([4,7,2,1,4], 2) = True
'''def esTroba(paco,x):
    if paco[0] == x:
        return True
    elif len(paco) == 1:
        return False
    else:
        return esTroba(paco[1:],x)
print(esTroba([4,7,2,1,4], 2))'''

#Crea una funció recursiva que donat un array de números en calculi la seva suma.
# Pe: sumaArray([1,3,7,4,5]) = 1+3+7+4+5 = 20 
'''def sumaArray(caca,x=None):
    if x == None:
        x = 0
    else:
        x += caca[0]
    if len(caca) == 1:
        return x
    return sumaArray(caca[1:],x)
print(sumaArray([1,3,7,4,5]))'''
#Crea una funció recursiva que calculi un sumatori des d’un número d’inici fins a un altre final.
#Pe: sumatori(3,8) = 3+4+5+6+7+8 = 33

while True:
    b = [int(numero) for numero in input().split()][:-1]
    if len(b) == 0:
        break
    z = [int(n) for n in input().split()]
    if b[z[0]-1] > b[z[1]-1]:
        print("JOANA")
    elif b[z[0]-1] < b[z[1]-1]:
        print("CARLOTA")