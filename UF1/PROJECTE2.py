from subprocess import run, call
from time import sleep

result = run(["ip","a"],capture_output=True,text=True)
linies = result.stdout.split("\n")
diccionari = {}
xarxa = []
xarxes = []
mask = []
scan = []
ports = {}
z = 0

for i in range(len(linies)):
    linies[i]=linies[i].strip()
    count = 0
    if (linies[i][:5]=="inet "):
        diccionari[linies[i].split(" ")[-1]] = linies[i].split(" ")[1]
        xarxa.append(linies[i].split(" ")[1].split("/")[0])
        mask.append(linies[i].split(" ")[1].split("/")[1])
        for i, c in enumerate(xarxa[z]):
            if c == ".":
                count += 1
            if count == (int(mask[z]) // 8):
                position = i
                xarxes.append(xarxa[z][:position]+".0"*(4-(int(mask[z]) // 8))+"/"+mask[z])
                scan.append(xarxa[z][:position]+".0"*(3-(int(mask[z]) // 8)))
                break
        z += 1

while True:
    try:
        print("\nOpcions: ")
        e = int()
        for i in diccionari:
            e += 1
            print("     Opció",str(e)+":","( Interfície:",i,"---> IP:",diccionari[i],")")
        resposta = int(input("\nEscull a quina adreça IP li vols realitzar-li un escaneig ping sweap a la seva xarxa (-sP): "))
    except ValueError:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    if 0 < resposta <= len(xarxa):
        call ('clear')
        print("Executant la següent comanda: nmap","-sP",xarxes[resposta-1])
        result=run(["nmap","-sP",xarxes[resposta-1]],capture_output=True,text=True)
        linies = result.stdout.split("\n")
        break
    else:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    
ip = list()
for i in range(len(linies)-1):
    if (linies[i][-1]==")"):
        ip.append(linies[i].split(" ")[-1][1:-1])
    elif scan[resposta-1] in linies[i].split()[-1]:
        ip.append(linies[i].split()[-1])
    else:
        continue

if len(ip) == 0:
        print("No hi ha cap equip disponible a la xarxa de la interfície seleccionada")
        sleep(3)
        exit()

while True:
    print("\nA quin equip vols realitzar-li un escaneig de ports?\n")
    a = int() 
    for i in ip:
        a += 1
        print("     Equip disponible "+str(a)+":",i)
    try:
        adreça = int(input("Resposta: "))
    except ValueError:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    if 0 < adreça <= len(ip):
        call ('clear')
        print("Executant la següent comanda: nmap","-sV",ip[adreça-1])
        result=run(["nmap","-sV",ip[adreça-1]],capture_output=True,text=True)
        linies = result.stdout.split("\n")
        break
    else:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    
for i in range(len(linies)):
    linies[i] = linies[i].split(" ")
    filtre_llista = [[x for x in e if x != ''] for e in linies]
    try:
        if filtre_llista[i][1] == 'open':
            ports[filtre_llista[i][0]] = filtre_llista[i][2:]
    except:
        continue
if len(ports) == 0:
        print("No hi ha cap port disponible per realitzar un escaneig.")
        sleep(3)
        exit()
        
port = list(ports)

while True:
    a = int()
    ver = str()
    p = []
    print("\nA quin port vols realitzar-li un escaneig de vulnearabilitats?\n")
    for i in port:
        for z in ports[i]:
            ver += str(z)+" "
        a += 1
        print("     Port disponible "+str(a)+":",i,"Versió:",ver)
        p.append(i.split("/")[0])
        ver = str()
    try:
        answer = int(input("Resposta: "))
    except ValueError:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    if 0 < answer <= len(ports):
        call ('clear')
        print("Executant la següent comanda: nmap","-sV","-sC","-p",p[answer-1],ip[adreça-1],"--script=vuln")
        result=run(["nmap","-sV","-sC","-p",p[answer-1],ip[adreça-1],"--script=vuln"])
        break
    else:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue