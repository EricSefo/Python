'''gfitxer = open("prova.txt")
cadena = gfitxer.readlines()
print(cadena[13],end="")'''
'''gfitxer = len(gfitxer.readlines())'''
'''count = 0
for i in gfitxer:
    print(i,end="")
    count += 1
print("\n\nEl fitxer té",count,"línies.")'''

'''try:
    contacte = open(input("Quin fitxer vols escollir? ")+".txt")
except:
    print("No existeix aquest fitxer!")
linia = contacte.read()
dic = linia.split()
dict = {}
for i in range (len(dic)):
    if i % 2 == 0:
        dict[dic[i+1]] = dic[i]
for n, i in enumerate (dict.items()):
    print(str(n+1)+".",i[1],i[0])
trucada = int(input("Escull un contacte de la llista per realitzar la trucada: "))
for n, (i,a) in enumerate (dict.items()):
    if n == trucada-1:
        print("Trucant a",i,"amb el número",str(a)+".")'''
        
try:
    llibre = input("Indicar quin fitxer vols obrir: ")
    num = open(llibre,"r")
except:
    print("El nom del fitxer no existeix:",llibre+".txt")
    exit()
paca = num.read()
puta = paca.split()
def generarXML(puta):
    global f
    f = open("fruites.txt","w")
    f.write("<fruites>\n")
    for i in range(len(puta)):
        f.write("\t<fruita>\n")
        f.write("\t\t"+str(puta[i])+"\n")
        f.write("\t</fruita>\n")
    f.write("</fruites>\n")
    f.close()
    return f
generarXML(puta)
puto = int()
for i in puta:
    try:
        puto += int(i)
    except:
        continue
num.close()
'''num.write("\nTOTAL: "+str(puto))
num.close()'''