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
val = list(diccionari.values())

while True:
    try:
        print("\nOpcions: ")
        e = int()
        for i in diccionari:
            e += 1
            print("     Opció",str(e)+":","( Interfície:",i,"   IP:",val[e-1],")")
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
    
print("\nA quin equip vols realitzar-li un escaneig de ports?\n")
a = int()   
for i in ip:
    a += 1
    print("     Equip disponible "+str(a)+":",i)

while True:
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
    try:
        if (linies[i][2]=="/") or (linies[i][3]=="/") or (linies[i][4]=="/"):
                ports[linies[i].split("/")[0]] = linies[i].split("   ")[-1]
    except:
        continue

ver = list(ports.values())
print(ver)
port = list(ports)
print("\nA quin port vols realitzar-li un escaneig de vulnearabilitats?\n")
a = int()

for i in port:
    a += 1
    print()
    print("     Port disponible "+str(a)+":",i)
    
while True:
    try:
        answer = int(input("Resposta: "))
    except ValueError:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
    if 0 < answer <= len(ports):
        call ('clear')
        print("Executant la següent comanda: nmap","-sV","-sC","-p",port[answer-1],ip[adreça-1])
        result=run(["nmap","-sV","-sC","-p",port[answer-1],ip[adreça-1]],capture_output=True,text=True)
        linies = result.stdout.strip().split("\n")
        break
    else:
        print("Introdueix una resposta correcta!")
        sleep(1)
        call ('clear')
        continue
print(linies)
    
'''print("Codi Retorn:\n",result.returncode)
print("Tipus error:\n ",result.stderr)'''