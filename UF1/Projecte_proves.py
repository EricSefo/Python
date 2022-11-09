import random

options = [ ["Pregunta 1: Dis-me l'arrel de quadrada de 4.",["1. 1.5\n","2. 2\n","3. 5\n"],2],
            ["Pregunta 2: Dis-me l'arrel de quadrada de 16.",["1. 4\n","2. 2\n","3. 6\n"],1],
            ["Pregunta 3: Quin és el record dels 100 metros llisos en segons?",["1. 9,58\n","2. 10\n","3. 9,78\n"],1],
            ["Pregunta 4: Quants milions de persones viuen a españa?",["1. 47\n","2. 50\n","3. 55\n"],1],
            ["Pregunta 5: En quin segle estem?",["1. 22\n","2. 20\n","3. 21\n"],3],
            ["Pregunta 6: Quin nivell d'anglès és el més alt?",["1. C2\n","2. C1\n","3. B2\n"],1],
            ["Pregunta 7: Quin edifici és el més alt del món?",["1. Burj Khalifa\n","2. Torre de Shanghái\n","3. One World Trade Center\n"],1],
            ["Pregunta 8: En quin any va acabar la segona guerra mundial?",["1. 1934\n","2. 1945\n","3. 1915\n"],2],
            ["Pregunta 9: Quin és millor mestre d'ASIX?",["1. Mireia\n","2. Jordi Varas\n","3. Gonçal\n"],3],
            ["Pregunta 10: Dis-me l'arrel quadrada de 25.",["1. 7\n","2. 5\n","3. 6\n"],2] ]

aleatori = random.choice(options)
response = options.index(aleatori)
random.shuffle(aleatori[1])
for i in range(len(pregunta)):
    print(str(i+1)+". "+aleatori[i][0])
    
print (aleatori[0]+"\n",StrA,StrB,StrC)

victoria_j1 = 0
victoria_j2 = 0
victoria_j3 = 0
victoria_j4 = 0

'''while True:
    partida = input("Amb quants jugadors vols jugar?\n Per triar una partida de dos jugadors escriu '2'\n Per triar una partida de quatre jugadors escriu '4'\n Elecció: ")
    if partida == "2":
        torn = random.randint(1, 2)
        break
    elif partida == "4":
        torn = random.randint(1, 4)
        print (torn)
        break
    else:
        print("Escriu correctament el nombre de jugadors!")
        continue

while True:
    if (victoria_j1 > 2) or (victoria_j2 > 2) or (victoria_j3 > 2) or (victoria_j4 > 2):
        print ("Ha guanyat el jugador",torn)
        break
    elif len(options) != 0:
        aleatori = random.choice(options)
        response = options.index(aleatori)
        random.shuffle(aleatori[1])
        StrA = "".join(aleatori[1][0])
        StrB = "".join(aleatori[1][1])
        StrC = "".join(aleatori[1][2])
        print (aleatori[0]+"\n"+StrA+StrB+StrC)
        if torn == 1: 
            answer = int(input("Jugador 1 (RESPOSTA): "))
            if answer == aleatori[2]:
                victoria_j1 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j1);
            else: 
                print("Resposta incorrecta!")
                torn = 2
        elif torn == 2:
            answer = int(input("Jugador 2 (RESPOSTA): "))
            if answer == aleatori[2]:
                victoria_j2 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j2);
            else: 
                print("Resposta incorrecta!")
                torn = 3
        elif torn == 3:
            answer = int(input("Jugador 3 (RESPOSTA): "))
            if answer == aleatori[2]:
                victoria_j3 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j3);
            else: 
                print("Resposta incorrecta!")
                torn = 4
        elif torn == 4:
            answer = int(input("Jugador 4 (RESPOSTA): "))
            if answer == aleatori[2]:
                victoria_j4 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j4);
            else: 
                print("Resposta incorrecta!")
                torn = 1
        del options[response]
    else:
        print("No hi ha més preguntes, el joc s'acabat")
        break'''