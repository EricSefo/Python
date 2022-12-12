#Escriviu un Script en python que en executar-se obtingui les ips de les interfícies 
# i crei un diccionari amb el nom de la interfície com a clau i la ip com a valor {
# ‘eth0’:’192.168.203.100/24’} L’script mostra els resultats per pantalla i l’usuari 
# pot escollir una d’aquestes 
# adreces per a fer un ping sweap a la XARXA amb nmap.
#S’emmagatzema els resultats de les ips disponibles en una llista.
#L’script mostra els resultats per pantalla i l’usuari pot escollir un equip per a realitzar 
# un escaneig de ports i les versions dels serveis que s’estan executant en ells. Els resultats 
# s’emmagatzemen en un diccionari amb el format {port:versio_servei}
#Els resultats es mostren per pantalla i l’usuari pot escollir un port per a realitzar 
# un escaneig de vulnerabilitats.

from subprocess import run, call

result = run(["ip","a"],capture_output=True,text=True)
linies = result.stdout.split("\n")
lxarxes = []
intxarxes = []
diccionari = {}
idllista = []

for i in range(len(linies)):
    linies[i]=linies[i].strip()
    if (linies[i][:5]=="inet "):
        diccionari[linies[i].split(" ")[-1]] = [linies[i].split(" ")[1]]

for i in diccionari.values():
    idllista.append(str(i[0]))
idllista[0] = str(idllista[0][:8]+"0"+idllista[0][9:])
idllista[1] = str(idllista[1][:12]+"0"+idllista[1][15:])
idllista[2] = str(idllista[2][:12]+"0"+idllista[2][13:])
idllista[3] = str(idllista[3][:9]+"0"+idllista[3][10:])
idllista[4] = str(idllista[4][:11]+"0"+idllista[4][12:])

while True:
    resposta = int(input("\nEscull a quina adreça de xarxa vols realitzar-li un escaneig ping sweap (-sP): \n"+
        "1. "+idllista[0]+"\n2. "+idllista[1]+"\n3. "+idllista[2]+"\n4. "+idllista[3]+"\n5. "+idllista[4]+"\nResposta: "))
    if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4 or resposta == 5:
        result=run(["nmap","-sP",idllista[resposta-1]],capture_output=True,text=True)
        print (result)
        break
    else:
        print("Introdueix una resposta correcta!")
        call ('clear')
        continue


'''lxarxes[0] = lxarxes[0][:11]
lxarxes[2] = lxarxes[2][:16]
lxarxes[3] = lxarxes[3][:13]
intxarxes[0] = intxarxes[0][7:]
intxarxes[2] = intxarxes[2][3:]
intxarxes[3] = intxarxes[3][2:]

for i in range (len(lxarxes)):
    dic = {intxarxes[i]:lxarxes[i]}
    print("Resultats:\n ",dic)
    xarxa = lxarxes[i][:9]
print (xarxa,0)'''

'''nmap = input ("Selecciona a quina xarxa vols realitzar-li un escaneig amb nmap: \n Opcions: ")
result=["nmap","-sP"],lxarxes [:12],0
print (result)'''

'''print("Codi Retorn:\n",result.returncode)
print("Tipus error:\n ",result.stderr)'''

'''
lxarxes [0]= lxarxes.replace('.1/8', '0')
'''
