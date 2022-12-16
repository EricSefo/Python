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
diccionari = {}
idllista = []
xarxa = []
mask = []

for i in range(len(linies)):
    linies[i]=linies[i].strip()
    if (linies[i][:5]=="inet "):
        diccionari[linies[i].split(" ")[-1]] = linies[i].split(" ")[1]

print (diccionari)

for i in diccionari:
    idllista.append(diccionari[i].split("/"))
    xarxa.append(diccionari[i].split("."))
    mask = int(idllista[0][1])
    print (mask)

print (xarxa,idllista)
    
'''while True:
    try:
        resposta = int(input("\nEscull a quina adreça de xarxa vols realitzar-li un escaneig ping sweap (-sP): \n"+
        "1. "+idllista[0][0]+"\n2. "+idllista[1][0]+"\n3. "+idllista[2][0]+"\n4. "+idllista[3][0]+"\nResposta: "))
    except TypeError:
        continue
    if resposta == 1 or resposta == 2 or resposta == 3 or resposta == 4 or resposta == 5:
        result=run(["nmap","-sP",idllista[resposta-1][0]],capture_output=True,text=True)
        linies = result.stdout.split("\n")
        print (linies)
        break
    else:
        print("Introdueix una resposta correcta!")
        call ('clear')
        continue'''

'''for i in range (len(lxarxes)):
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