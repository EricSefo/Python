preguntes =[ ["Pregunta 1: Dis-me l'arrel de quadrada de 4.\n1. 1.5\n 2. 2\n 3. 5", 2]
["Pregunta 2: Dis-me l'arrel de quadrada de 16.\n 1. 4\n 2. 2\n 3. 6",1]
["Pregunta 3: Quin és el record dels 100 metros llisos en segons?\n 1. 9,58\n 2. 10\n 3. 9,78",1]
["Pregunta 4: Quants milions de persones viuen a españa?\n 1. 47\n 2. 50\n 3. 55",1]
["Pregunta 5: En quin segle estem?\n 1. 22\n 2. 20\n 3. 21",3]
["Pregunta 6: Quin nivell d'anglès és el més alt?\n 1. C2\n 2. C1\n 3. B2",1]
["Pregunta 7: Quin edifici és el més alt del món?\n 1. Burj Khalifa\n 2. Torre de Shanghái\n 3. One World Trade Center",1]
["Pregunta 8: En quin any va acabar la segona guerra mundial?\n 1. 1934\n 2. 1945\n 3. 1915",2]
["Pregunta 9: Quin és millor mestre de ASIX?\n 1. Mireia\n 2.Jordi Varas\n 3. Gonçal",3]
["Pregunta 10: Dis-me l'arrel de quadrada de 25.\n 1. 7\n 2. 5\n 3. 6",2] ]

res=int(input("\nQuina és la resposta correcta?"))
if (res==preguntes[0][1]):
    print("Felicitats")
else:
    print("L'has cagat")

#Dos jugadors, el primer que encerta 3 preguntes guanya!!
#El format de les preguntes serà:
#Enunciat pregunta:
#Resposta 1
#Resposta 2
#Resposta 3
#S'ha de mostrar un marcador de preguntes encertades per cada jugador.
#Cada jugador anirà responent preguntes fins que falli.
#El torn d'inici serà aleatori.
#Si S'han realitzat 10 preguntes i no hi ha guanyador el joc acaba.
#Les preguntes es mostraran en ordre aleatori.
#Heu de controlar quines preguntes ja s'han plantejat als jugadors.

#OPCIONAL:
#Les respostes es mostraran en ordre aleatori.
#Podem escollir el nombre de jugadors entre 2 i 4