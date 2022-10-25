import random
num = random.randint(1,100)
contador = 5
while contador > 0:
    candidat=int(input("Adivina el número entre 0 i 100: "))  
    if num > candidat:
        print("El número és més mejor a",candidat)
    elif num < candidat:
        print("El número és més menor a",candidat)
    elif num == candidat:
        print("Has acertat el número!")
        break
    contador -= 1
print("S'han acabat els intents")

pesos = {'Pepe':[56, 64, 54],
         'Paco':[89, 87, 86], 
         'Pancracio':[102, 105, 111]}
    