import random
llista = []

for i in range(4):
    x = int(input())
    if x != 0:
        llista.append(x)
        print (llista)
    else:
        carlota = random.choice(llista)
        remove = llista.index(carlota)
        del llista[remove]
        joana = random.choice(llista)
        remove = llista.index(joana)
        del llista[remove]
        print (carlota,joana)