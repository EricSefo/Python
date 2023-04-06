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
    
def conversio(p,w,x=None):
    global z
    global q
    global y
    if w == decimal:
        for i in x.split("."):
            z = int()
            q = int()
            p += str(w(i))
            if p.count(".") < 3:
                p += "."
        return p
    elif w == binari:
        for i in list(map(int ,input("IP: ").split("."))):
            y = str()
            p += w(i)
            if p.count(".") < 3:
                p += "."
        return p
    
def autocompletar(x):
    while (x.count("1") + x.count("0")) != 32:
        if (x.count("1") + x.count("0")) % 8 == 0:
            x += '.'
        x += '0'
    return x

a = str()
b = str()
a = conversio(a,binari)
b = conversio(b,decimal,a)

masc = int(input("Màscara de xarxa: "))
if masc >= 0 and masc <= 32:
    masc_binari = str()
    for i in range (masc):
        masc_binari += '1'
        if masc_binari.count("1") % 8 == 0:
            masc_binari += '.'
    masc_binari = autocompletar(masc_binari)
else:
    print("Màscara incorrecta")
    exit()

decimal_masc = str()
decimal_masc = conversio(decimal_masc,decimal,masc_binari)

if 0 <= int(b.split(".")[0]) <= 127 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b,a,"\nClasse A\n"+"Màscara:",masc_binari,"=",masc,decimal_masc)
elif 128 <= int(b.split(".")[0]) <= 191 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b,a,"\nClasse B\n"+"Màscara:",masc_binari,"=",masc,decimal_masc)
elif 192 <= int(b.split(".")[0]) <= 223 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b,a,"\nClasse C\n"+"Màscara:",masc_binari,"=",masc,decimal_masc)
elif 224 <= int(b.split(".")[0]) <= 239 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b,a,"\nClasse D (Multicast)\n"+"Màscara:",masc_binari,"=",masc,decimal_masc)
elif 240 <= int(b.split(".")[0]) <= 255 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
    print("Adreça IP:",b,a,"\nClasse E (experimental)\n"+"Màscara:",masc_binari,"=",masc,decimal_masc)
else:
    print("IP incorrecta")
    exit()

count=int()
for i, c in enumerate(a): # "i" val la posició del element en la llista i "c" és cada caràcter de l'adreça IP per contar els punts
    if c == '1' or c == '0':
        count += 1
        if count == masc:
            a = a[:i+1]
            a = autocompletar(a)
            xarxa = str()
            xarxa = conversio(xarxa,decimal,a)
print(a,xarxa)