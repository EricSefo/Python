import random
jugador1 = input()
jugador2 = input()

jugadors = [jugador1,jugador2]
contador = [0,0]
paco = random.randint(0,1)
player = jugadors[paco]
print (player)
print ("Pregunta:")
answer = input("Resposta:")
resposta = ["a","b"]
if answer == resposta[1]:
    print("correcte")
    contador += 1
    print (contador)
