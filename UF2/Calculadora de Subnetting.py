# Inicialitza la variable y com una cadena buida
def binari(x):  # Defineix la funció binari que pren un paràmetre x
    global y  # Indica que es farà servir la variable y definida fora de la funció
    y += str(x % 2)  # Afegeix el residu de dividir x per 2 a la cadena y, convertint-ho primer a cadena amb la funció str()
    if x < 2:  # Si x és menor a 2
        while len(y) < 8:
            y += '0'
        return y[::-1] # Retorna la cadena y invertida (ja que s'ha afegit el bit menys significatiu primer)
    else:  # Altrament
        return binari(x // 2)  # Retorna el resultat de cridar la funció binari amb el quocient de dividir x entre 2

def decimal(x):
    global z
    global q
    if len(x) == 0:
        return q
    else:
        q += int(x[-1])*(2**z)
        z += 1
        return decimal(x[:-1])

a = str()
b = str()
for i in list(map(int ,input("IP: ").split("."))):
    y = str()
    a += binari(i)+"."
for i in a[:-1].split("."):
    z = int()
    q = int()
    b += str(decimal(i))+"."
masc = int(input("Màscara de xarxa: "))
if masc >= 0 and masc <= 32:
    binari = str()
    for i in range (masc):
        binari += '1'
        if binari.count("1") % 8 == 0:
            binari += '.'
    while (binari.count("1") + binari.count("0")) != 32:
        if (binari.count("1") + binari.count("0")) % 8 == 0:
            binari += '.'
        binari += '0'
else:
    print("Màscara incorrecta")

decimal_masc = str()
for i in binari.split("."):
    z = int()
    q = int()
    decimal_masc += str(decimal(i))+"."

if 0 <= int(b.split(".")[0]) <= 127 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b[:-1],a[:-1],"\nClasse A\n"+"Màscara:",binari,decimal_masc[:-1])
elif 128 <= int(b.split(".")[0]) <= 191 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b[:-1],a[:-1],"\nClasse B\n"+"Màscara:",binari,decimal_masc[:-1])
elif 192 <= int(b.split(".")[0]) <= 223 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b[:-1],a[:-1],"\nClasse C\n"+"Màscara:",binari,decimal_masc[:-1])
elif 224 <= int(b.split(".")[0]) <= 239 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b[:-1],a[:-1],"\nClasse D (Multicast)\n"+"Màscara:",binari,decimal_masc[:-1])
elif 240 <= int(b.split(".")[0]) <= 255 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b[:-1],a[:-1],"\nClasse E (experimental)\n"+"Màscara:",binari,decimal_masc[:-1])
else:
    print("IP incorrecta")

count=int()
for i, c in enumerate(b[:-1]): # "i" val la posició del element en la llista i "c" és cada caràcter de l'adreça IP per contar els punts
    pass
print(b)