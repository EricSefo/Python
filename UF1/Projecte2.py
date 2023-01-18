from subprocess import run, call
from time import sleep

result = run(["ip","a"],capture_output=True,text=True)
linies = result.stdout.split("\n")
diccionari = {}

for i in range(len(linies)):
    linies[i]=linies[i].strip()
    if (linies[i][:5]=="inet "):
        diccionari[linies[i].split(" ")[-1]] = linies[i].split(" ")[1]
val = list(diccionari.values())

for i in diccionari:
    mask = str(diccionari[i].split("/")[-1])
    diccionari.update({i:(diccionari[i].split("/")[0][:-1]+"0")})
    if diccionari[i][-2] != ".":
        diccionari.update({i:(diccionari[i][:-3]+"0")})
    for e in range(1):
        diccionari.update({i:(diccionari[i]+"/"+mask)})
val2 = list(diccionari.values())

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
    if 0 < resposta <= len(val2):
        call ('clear')
        print("Executant la següent comanda: nmap","-sP",val2[resposta-1])
        result=run(["nmap","-sP",val2[resposta-1]],capture_output=True,text=True)
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
    linies[i]=linies[i].strip()
    if (linies[i][2]=="/"):
        diccionari[linies[i][2].split("/")[0]] = linies[i].split(" ")[3:]
print(diccionari)
'''print("Codi Retorn:\n",result.returncode)
print("Tipus error:\n ",result.stderr)'''