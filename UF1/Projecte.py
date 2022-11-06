import random
from random import randint, choice

preguntes = ["Pregunta 1: Dis-me l'arrel de quadrada de 4.", 
"Pregunta 2: Dis-me l'arrel de quadrada de 16.",
"Pregunta 3: Quin és el record dels 100 metros llisos en segons?",
"Pregunta 4: Quants milions de persones viuen a españa?",
"Pregunta 5: En quin segle estem?",
"Pregunta 6: Quin nivell d'anglès és el més alt?",
"Pregunta 7: Quin edifici és el més alt del món?",
"Pregunta 8: En quin any va acabar la segona guerra mundial?",
"Pregunta 9: Quin és millor mestre d'ASIX?",
"Pregunta 10: Dis-me l'arrel quadrada de 25."]

respostes = ["1. 1.5\n2. 2\n3. 5", 
            "1. 4\n2. 2\n3. 6",
            "1. 9,58\n2. 10\n3. 9,78",
            "1. 47\n2. 50\n3. 55",
            "1. 22\n2. 20\n3. 21",
            "1. C2\n2. C1\n3. B2",
            "1. Burj Khalifa\n2. Torre de Shanghái\n3. One World Trade Center",
            "1. 1934\n2. 1945\n3. 1915",
            "1. Mireia\n2. Jordi Varas\n3. Gonçal",
            "1. 7\n2. 5\n3. 6"]

correcta = [2,1,1,1,3,1,1,2,3,2]

victoria_j1 = 0
victoria_j2 = 0
torn = random.randint(1, 2)

while True:
    if (victoria_j1 > 2) or (victoria_j2 > 2):
        print ("Ha guanyat el jugador",torn)
        break
    elif len(preguntes) != 0:
        pregunta = random.choice(preguntes)
        response = preguntes.index(pregunta)
        print (pregunta)
        preguntes.remove(pregunta)
        eliminar_resposta = (respostes[response])
        print (eliminar_resposta)
        respostes.remove(eliminar_resposta)
        if torn == 1:
            answer = int(input("Jugador 1 (RESPOSTA): "))
            if answer == correcta[response]:
                victoria_j1 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j1);
            else: 
                print("Resposta incorrecta!")
                torn = 2
        elif torn == 2:
            answer = int(input("Jugador 2 (RESPOSTA): "))
            if answer == correcta[response]:
                victoria_j2 += 1
                print("Resposta correcta!\n --- MARCADOR ---\n Preguntes encertades :",victoria_j2);
            else: 
                print("Resposta incorrecta!")
                torn = 1
        del correcta[response]    
    else:
        print("No hi ha més preguntes, el joc s'acabat")
        break
    

'''#Dos jugadors, el primer que encerta 3 preguntes guanya!!'''
'''#El format de les preguntes serà:
#Enunciat pregunta:
#Resposta 1
#Resposta 2
#Resposta 3'''
'''#S'ha de mostrar un marcador de preguntes encertades per cada jugador.'''
'''# Cada jugador anirà responent preguntes fins que falli.'''
'''#El torn d'inici serà aleatori.'''
'''#Si S'han realitzat 10 preguntes i no hi ha guanyador el joc acaba.'''
'''#Les preguntes es mostraran en ordre aleatori.'''
'''#Heu de controlar quines preguntes ja s'han plantejat als jugadors.'''

#OPCIONAL:
#Les respostes es mostraran en ordre aleatori.
#Podem escollir el nombre de jugadors entre 2 i 4