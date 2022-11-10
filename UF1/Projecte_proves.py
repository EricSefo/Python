import random

options = [ ["Pregunta 1: Dis-me l'arrel de quadrada de 4.",["1.5","2","5"],"2"],
            ["Pregunta 2: Dis-me l'arrel de quadrada de 16.",["4","2","6"],"1"],
            ["Pregunta 3: Quin és el record dels 100 metros llisos en segons?",["9,58","10","9,78"],"1"],
            ["Pregunta 4: Quants milions de persones viuen a españa?",["47","50","55"],"1"],
            ["Pregunta 5: En quin segle estem?",["22","20","21"],"3"],
            ["Pregunta 6: Quin nivell d'anglès és el més alt?",["C2","C1","B2"],"1"],
            ["Pregunta 7: Quin edifici és el més alt del món?",["Burj Khalifa","Torre de Shanghái","One World Trade Center"],"1"],
            ["Pregunta 8: En quin any va acabar la segona guerra mundial?",["1934","1945","1915"],"2"],
            ["Pregunta 9: Quin és millor mestre d'ASIX?",["Mireia","Jordi Varas","Gonçal"],"3"],
            ["Pregunta 10: Dis-me l'arrel quadrada de 25.",["7","5","6"],"2"] ]

victoria_j1 = 0
victoria_j2 = 0
victoria_j3 = 0
victoria_j4 = 0

while True:
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
        print (aleatori[0])
        for i in range(len(aleatori[1])):
            print(str(i+1)+". "+aleatori[1][i])
        if partida == "2":
            if torn == 1: 
                answer = input("Jugador 1 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j1 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j1);
                else: 
                    print("Resposta incorrecta!")
                    torn = 2
            elif torn == 2:
                answer = input("Jugador 2 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j2 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j2);
                else: 
                    print("Resposta incorrecta!")
                    torn = 1
        elif partida == "4":
            if torn == 1: 
                answer = input("Jugador 1 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j1 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j1);
                else: 
                    print("Resposta incorrecta!")
                    torn = 2
            elif torn == 2:
                answer = input("Jugador 2 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j2 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j2);
                else: 
                    print("Resposta incorrecta!")
                    torn = 3
            elif torn == 3:
                answer = input("Jugador 3 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j3 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j3);
                else: 
                    print("Resposta incorrecta!")
                    torn = 4
            elif torn == 4:
                answer = input("Jugador 4 (RESPOSTA): ")
                if answer == aleatori[2]:
                    victoria_j4 += 1
                    print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j4);
                else: 
                    print("Resposta incorrecta!")
                    torn = 1
        del options[response]
    else:
        print("No hi ha més preguntes, el joc s'acabat")
        break