acumular = int()
acumular2 = int()
k = int(input())
producte = 1
if k > 0:
    for valors in range (k):
        n = int(input())
        if n > 0:
            for valor in range (n):
                n += valor
                producte *= valor+1
            print ("SUMA: ",n,"PRODUCTE: ",producte)
            producte = 1
        else:
            print("ELS NOMBRES NATURALS COMENCEN EN 1")