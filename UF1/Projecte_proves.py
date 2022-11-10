import random

options = [ ["Pregunta 1: Dis-me l'arrel de quadrada de 4.", [["1.5",False],["2",True],["5",False]]],
            ["Pregunta 2: Dis-me l'arrel de quadrada de 16.", [["4",True],["2",False],["6",False]]],
            ["Pregunta 3: Quin és el record dels 100 metros llisos en segons?", [["9,58",True],["10",False],["9,78",False]]],
            ["Pregunta 4: Quants milions de persones viuen a españa?", [["47",True],["50",False],["55",False]]],
            ["Pregunta 5: En quin segle estem?", [["22",False],["20",False],["21",True]]],
            ["Pregunta 6: Quin nivell d'anglès és el més alt?",[["C2",True],["C1",False],["B2",False]]],
            ["Pregunta 7: Quin edifici és el més alt del món?",[["Burj Khalifa",True],["Torre de Shanghái",False],["One World Trade Center",False]]],
            ["Pregunta 8: En quin any va acabar la segona guerra mundial?",[["1934",False],["1945",True],["1915",False]]],
            ["Pregunta 9: Quin és millor mestre d'ASIX?",[["Mireia",False],["Jordi Varas",False],["Gonçal",True]]],
            ["Pregunta 10: Dis-me l'arrel quadrada de 25.",[["7",False],["5",True],["6",False]]] ]


victorias = [0, 0, 0, 0]

while True:
    partida = int(input("Amb quants jugadors vols jugar?\n Per triar una partida de dos jugadors escriu '2'\n Per triar una partida de quatre jugadors escriu '4'\n Elecció: "))

    if partida == 2 or partida == 4:
        torn = random.randint(1, partida)
        break
    else:
        print("Escriu correctament el nombre de jugadors!")
        continue

while True:
    if (victorias[0] > 2) or (victorias[1] > 2) or (victorias[2] > 2) or (victorias[3] > 2):
        print ("Ha guanyat el jugador", torn)
        break
    elif len(options) != 0:
        aleatori = random.choice(options)
        response = options.index(aleatori)
        random.shuffle(aleatori[1])
        print (aleatori[0])
        for i in range(3):
            print(str(i+1)+". ",aleatori[1][i][0])

        answer = int(input("Jugador " + str(torn) + " (RESPOSTA): "))
        if aleatori[1][answer - 1][1] == True:
            victorias[torn] += 1
            print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :", victorias[torn])
        else: 
            print("Resposta incorrecta!\n")
            if (torn == partida): 
                torn = 1
            else: 
                torn += 1
            print ("--- CANVI DE TORN ---\n")

        del options[response]
    else:
        print("No hi ha més preguntes, el joc s'acabat")
        break