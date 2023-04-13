# Importem el mòdul tkinter
from tkinter import *
from tkinter import messagebox

# Inicialitzem la variable y com una cadena buida
def binari(x):
    # Indiquem que s'utilitzarà la variable y definida fora de la funció
    global y
    # Afegim el residu de dividir x per 2 a la cadena y, convertint-lo primer a cadena amb la funció str()
    y += str(x % 2)
    # Si x és menor a 2
    if x < 2:
        # Omplim la cadena y amb zeros
        while len(y) < 8:
            y += '0'
        # Retornem la cadena y invertida (ja que s'ha afegit el bit menys significatiu primer)
        return y[::-1]
    # Si x no és menor a 2
    else:
        # Retornem el resultat de cridar la funció binari amb el quocient de dividir x entre 2
        return binari(x // 2)

# Funció que converteix un nombre en binari a decimal
def decimal(x):
    global z  # Fem servir la variable z definida fora de la funció
    global q  # Fem servir la variable q definida fora de la funció
    if len(x) == 0:  # Si la longitud de la cadena x és 0
        return q  # Retorna el valor de la variable q
    else:
        q += int(x[-1])*(2**z)  # Converteix l'últim dígit de la cadena x a un enter i el multiplica per 2 elevat a la variable z, i afegeix el resultat a la variable q
        z += 1  # Incrementa la variable z en 1
        return decimal(x[:-1])  # Retorna el resultat de cridar la funció decimal amb tots els dígits menys l'últim de la cadena x

# Funció que converteix un nombre en binari o un conjunt de nombres separats per punts en un nombre en decimal o un conjunt de nombres separats per punts
def conversio(p,w,x):
    global z  # Fem servir la variable z definida fora de la funció
    global q  # Fem servir la variable q definida fora de la funció
    global y  # Fem servir la variable y definida fora de la funció
    if w == decimal:  # Si el paràmetre w és la funció decimal
        for i in x.split("."):  # Per a cada part de la cadena x separada per punts
            z = int()  # Reinicialitza la variable z a 0
            q = int()  # Reinicialitza la variable q a 0
            p += str(w(i))  # Afegeix la conversió de la part actual a decimal a la cadena p
            if p.count(".") < 3:  # Si la cadena p no té més de 2 punts
                p += "."  # Afegeix un punt a la cadena p
        return p  # Retorna la cadena p
    elif w == binari:  # Si el paràmetre w és la funció binari
        for i in list(map(int ,x.split("."))):  # Per a cada part de la cadena x separada per punts convertida a un enter
            y = str()  # Reinicialitza la variable y a una cadena buida
            p += w(i)  # Afegeix la conversió de la part actual a binari a la cadena p
            if p.count(".") < 3:  # Si la cadena p no té més de 2 punts
                p += "."  # Afegeix un punt a la cadena p
        return p  # Retorna la cadena p
    
# Definició de la funció "autocompletar"
def autocompletar(x, y, z):
    # Es continua el bucle mentre la suma de 0 i 1 de "x" no sigui igual a "y"
    while (x.count("1") + x.count("0")) != y:
        # Si la suma de 0 i 1 de "x" és múltiple de 8 i "x" té una longitud més gran que 0
        if (x.count("1") + x.count("0")) % 8 == 0 and len(x) > 0:
            # S'afegeix un punt (".") a "x"
            x += '.'
        # S'afegeix "z" a "x"
        x += z
    # Es retorna "x"
    return x

# Variables globals
classe = str()
tipus = "Pública"
hosts = int()

# Definició de la funció "calcular"
def calcular():
    # Variables locals
    a = str()
    b = str()
    masc_binari = str()
    wildcard = str()
    decimal_masc = str()
    count = int()
    ip = str()
    host_max = str()
    broadcast = str()
    xarxa = str()
    host_min = str()
    
    # Variables globals
    global classe
    global tipus
    global hosts
    
    # Es guarda la cadena de text introduïda per l'usuari en "adreça"
    adreça = ent1.get()
    try:
        if adreça.count(".") == 3 and 0 <= int(adreça.split(".")[0]) <= 255 and 0 <= int(adreça.split(".")[1]) <= 255 and 0 <= int(adreça.split(".")[2]) <= 255 and 0 <= int(adreça.split(".")[3]) <= 255:
            # Si l'adreça IP és vàlida, es converteix a binari i després a decimal
            a = conversio(a,binari,adreça)
            b = conversio(b,decimal,a)
        else:
            # Si l'adreça IP no és vàlida, es genera una excepció
            raise ValueError
    except:
        # En cas que hi hagi una excepció, es mostra un missatge d'error
        messagebox.showinfo("IP incorrecta", "IP incorrecta")

    try:
        # S'intenta llegir la màscara de xarxa
        masc = int(ent2.get())
    except:
        # Si la màscara no es pot llegir, es mostra un missatge d'error
        messagebox.showinfo("Màscara incorrecta", "Màscara incorrecta")

    if masc >= 0 and masc <= 30:
        # Si la màscara és vàlida, es converteix a binari i es genera la wildcard
        masc_binari = autocompletar(masc_binari,masc,"1")
        binari_wildcard = masc_binari.replace("1","0")
        binari_wildcard = autocompletar(binari_wildcard,32,"1")
        masc_binari = autocompletar(masc_binari,32,"0")
    else:
        # Si la màscara no és vàlida, es mostra un missatge d'error
        messagebox.showinfo("Màscara incorrecta", "Màscara incorrecta")

    # Es converteix la wildcard i la màscara de xarxa a decimal
    wildcard = conversio(wildcard,decimal,binari_wildcard)
    decimal_masc = conversio(decimal_masc,decimal,masc_binari)
    for i, c in enumerate(a):  # per a cada caràcter i índex de la cadena a
        if c == '1' or c == '0':  # si el caràcter és 1 o 0
            count += 1  # augmenta el comptador en 1
            if count == masc:  # si el comptador és igual a la màscara
                ip = a[:i+1]  # guarda la cadena fins a la posició i+1 com a adreça IP
                hosts = 2**(32 - (ip.count("1") + ip.count("0")))-2  # calcula el nombre d'amfitrions possibles
                binari_host_max = autocompletar(ip,31,"1")+"0"  # obté l'adreça del darrer amfitrió
                binari_broadcast = autocompletar(ip,32,"1")  # obté l'adreça de difusió
                host_max = conversio(host_max,decimal,binari_host_max)  # converteix l'adreça del darrer amfitrió a decimal
                broadcast = conversio(broadcast,decimal,binari_broadcast)  # converteix l'adreça de difusió a decimal
                ip = autocompletar(ip,32,"0")  # completa l'adreça IP amb zeros fins a 32 bits
                xarxa = conversio(xarxa,decimal,ip)  # converteix l'adreça de xarxa a decimal
    binari_host_min = ip[:-1]+"1"  # obté l'adreça del primer amfitrió
    host_min = conversio(host_min,decimal,binari_host_min)  # converteix l'adreça del primer amfitrió a decimal
    try:
        nova_mascara = int(ent3.get())  # obté la nova màscara introduïda per l'usuari
        if nova_mascara >= 0 and nova_mascara <= 30 and nova_mascara > masc:  # si la nova màscara és vàlida
            bits = nova_mascara - masc  # calcula el nombre de bits addicionals per a la nova màscara
            subxarxes_mascara = str(2**bits)  # calcula el nombre de subxarxes possibles
            l23.config(text="Subxarxes de la nova màscara: "+subxarxes_mascara+" subxarxes amb "+str(2**(32-nova_mascara)-2)+" hosts cadascuna.")
        else:
            messagebox.showinfo("Màscara nova incorrecta", "Màscara nova incorrecta perquè el seu valor ha d'estar entre 0 i 30, també ha de ser major que la màscara per defecte.")
    except:
        l23.config(text="")  # si hi ha un error, no mostra cap informació sobre les subxarxes possibles
        
    try:
        subxarxes_requerides = int(ent4.get()) # Obtenim el número de subxarxes requerides a partir de l'entrada ent4
        if subxarxes_requerides < 1: # Si el número de subxarxes requerides és menor que 1, no cal fer cap càlcul
            l24.config(text="Es necessiten 0 bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides.")
        else:
            for i in range (31-masc): # Per a cada possible valor de bits de màscara addicionals
                subxarxes = 2**i # Calculem el número de subxarxes que es poden crear amb aquest valor de bits addicionals
                if subxarxes_requerides <= subxarxes: # Si el número de subxarxes requerides és menor o igual al número de subxarxes que es poden crear amb aquest valor de bits addicionals
                    l24.config(text="Es necessiten "+str(i)+" bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides. En total es crearan "+str(2**i)+ " subxarxes amb "+str(2**(32-(i+masc))-2)+" hosts cadascuna. La nova màscara seria /"+str(masc+i)+".") # Mostrem la informació corresponent a aquesta configuració de subxarxes
                    break # Sortim del bucle ja que ja hem trobat la solució
            if subxarxes_requerides > subxarxes: # Si el número de subxarxes requerides és més gran que el número màxim de subxarxes que es poden crear amb la màscara actual
                l24.config(text="No hi ha prous bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides.") # Mostrem un missatge d'error
    except:
        l24.config(text="") # Si hi ha algun error, no mostrem cap informació a la pantalla
 
    # Intentam llegir el nombre de hosts requerits
    try:
        hosts_requerits = int(ent5.get())
        # Si el nombre de hosts requerits és menor que 1, no calen bits addicionals
        if hosts_requerits < 1:
            l25.config(text="Es necessiten 0 bits per obtenir els "+str(hosts_requerits)+" hosts requerits.")
        else:
            # Iteram sobre el nombre de bits addicionals necessaris
            for i in range (32-masc):
                # Calculem el nombre de hosts per subxarxa per la quantitat de bits addicionals actuals
                hosts_subxarxa = (2**i)-2
                # Si els hosts requerits són menors o iguals que els hosts per subxarxa actuals, hem trobat la solució
                if hosts_requerits <= hosts_subxarxa:
                    l25.config(text="Es necessiten "+str(i)+" bits per obtenir els "+str(hosts_requerits)+" hosts requerits en "+str(2**(32-(i+masc)))+" subxarxes amb "+str(hosts_subxarxa)+" hosts per subxarxa en total. La nova màscara seria /"+str(masc+(32-(i+masc)))+".")
                    break
            # Si no hem trobat solució, no hi ha prou bits addicionals
            if hosts_requerits > hosts_subxarxa:
                l25.config(text="No hi ha prous bits per obtenir els "+str(hosts_requerits)+" hosts requerits.")
    # Si hi ha un error, deixam el text del resultat en blanc
    except:
        l25.config(text="")

    # Comprovam si l'adreça IP és de classe A
    if 0 <= int(b.split(".")[0]) <= 127 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 10 == int(b.split(".")[0]) and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada" # si l'adreça comença per 10.x.x.x és una adreça privada
        classe = "Classe A"

    # Comprovam si l'adreça IP és de classe B
    elif 128 <= int(b.split(".")[0]) <= 191 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 172 == int(b.split(".")[0]) and 16 <= int(b.split(".")[1]) <= 31 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada" # si l'adreça comença per 172.16.x.x - 172.31.x.x és una adreça privada
        classe = "Classe B"

    # Comprovam si l'adreça IP és de classe C
    elif 192 <= int(b.split(".")[0]) <= 223 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 192 == int(b.split(".")[0]) and 168 == int(b.split(".")[1]) and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada" # si l'adreça comença per 192.168.x.x és una adreça privada
        classe = "Classe C"

    # Comprovam si l'adreça IP és de classe D
    elif 224 <= int(b.split(".")[0]) <= 239 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        classe = "Classe D"

    # Comprovam si l'adreça IP és de classe E
    elif 240 <= int(b.split(".")[0]) <= 255 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        classe = "Classe E"

    # Si l'adreça IP no pertany a cap classe coneguda, mostrem un missatge d'error
    else:
        messagebox.showinfo("IP incorrecta", "IP incorrecta",ip,b)

    l7.config(text="Adreça: "+b) # Configura l'etiqueta l7 amb l'adreça IP
    l8.config(text=a) # Configura l'etiqueta l8 amb el nom del host
    l9.config(text="Màscara: "+decimal_masc+" = "+(str(masc))) # Configura l'etiqueta l9 amb la màscara en format decimal i binari
    l10.config(text=masc_binari,fg="red") # Configura l'etiqueta l10 amb la màscara en format binari i color vermell
    l11.config(text="Màscara Wildcard: "+wildcard) # Configura l'etiqueta l11 amb la màscara Wildcard
    l12.config(text=binari_wildcard) # Configura l'etiqueta l12 amb la màscara Wildcard en format binari
    l13.config(text="Xarxa: "+xarxa) # Configura l'etiqueta l13 amb l'adreça de xarxa
    l14.config(text=ip) # Configura l'etiqueta l14 amb l'adreça IP
    l15.config(text="Host Mínim: "+host_min) # Configura l'etiqueta l15 amb l'adreça del primer host
    l16.config(text=binari_host_min) # Configura l'etiqueta l16 amb l'adreça del primer host en format binari
    l17.config(text="Host Màxim: "+host_max) # Configura l'etiqueta l17 amb l'adreça del darrer host
    l18.config(text=binari_host_max) # Configura l'etiqueta l18 amb l'adreça del darrer host en format binari
    l19.config(text="Broadcast: "+broadcast) # Configura l'etiqueta l19 amb l'adreça de broadcast
    l20.config(text=binari_broadcast) # Configura l'etiqueta l20 amb l'adreça de broadcast en format binari
    l21.config(text="Hosts per xarxa: "+str(hosts)) # Configura l'etiqueta l21 amb el número de hosts per xarxa
    l22.config(text=classe+", "+tipus,fg="blue") # Configura l'etiqueta l22 amb la classe i el tipus de xarxa

def clear():
    ent1.delete(0,END) # Esborra l'entrada d'adreça IP
    ent2.delete(0,END) # Esborra l'entrada de màscara de xarxa
    ent3.delete(0,END) # Esborra l'entrada de prefix de xarxa
    ent4.delete(0,END) # Esborra l'entrada de nombre de subxarxes
    ent5.delete(0,END) # Esborra l'entrada de nombre de hosts per subxarxa
    for i in range (7,26): # Bucle que recorre les etiquetes de l'aplicació
        exec(f"l{i}.config(text='')") # Esborra el contingut de les etiquetes

# Creem una finestra principal per a l'aplicació
win = Tk()

# Establim la mida de la finestra
win.geometry("1500x600")

# Establim el color de fons de la finestra
win.configure(bg = '#e8e4e4')

# Establim el títol de la finestra
win.title('Calculadora IP')

# Creem una etiqueta per al títol
l0 = Label(text="Calculadora IP", fg="blue", bg="#e8e4e4",border=15, font=("Arial", 25, "bold"))
l0.place(x=580,y=0)

# Creem etiquetes i camps d'entrada per a les dades
l1 = Label(text="Adreça (Host o Xarxa):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l1.place(x=47,y=70)
ent1 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent1.place(x=50,y=100)

l2 = Label(text="Màscara:", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l2.place(x=247,y=70)
ent2 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent2.place(x=250,y=100)

l3 = Label(text="Màscara per subxarxes (opcional):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l3.place(x=447,y=70)

l4 = Label(text="moure a:", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l4.place(x=447,y=100)
ent3 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent3.place(x=525,y=100)

l5 = Label(text="Número de subxarxes requerides (opcional):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l5.place(x=722,y=70)
ent4 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white",width=28)
ent4.place(x=725,y=100)

l6 = Label(text="Número de hosts requerits (opcional):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4")
l6.place(x=1082,y=70)
ent5 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white",width=28)
ent5.place(x=1085,y=100)

# Creem botons per a les accions de càlcul i neteja
btn1 = Button(text="Calcular", command=calcular, font=("Arial", 12), bg="#e8e4e4") 
btn1.place(x=50,y=130)

btn2 = Button(text="Llimpiar", command=clear, font=("Arial", 12), bg="#e8e4e4") 
btn2.place(x=130,y=130)

# Inicialitzem la variable posy
posy = int()

# Iterem del 7 al 25 (ambdós inclosos)
for i in range (7,26):
    
    # Inicialitzem la variable posx
    posx = int()
    
    # Si i és major que 22, posx serà 0 i posy s'incrementarà en 50
    if i > 22:
        posx = 0
        posy += 50
    
    # Si i és parell, posx s'incrementarà en 280; si no, posy s'incrementarà en 20
    else:
        if i % 2 == 0:
            posx += 280
        else:
            posy += 20
    
    # Creem una etiqueta amb un número identificador i la configurem
    exec(f"l{i} = Label(font=('Arial', 12, 'bold'), fg='black', bg='#e8e4e4')")
    
    # Posicionem l'etiqueta a la finestra amb les coordenades corresponents
    exec(f"l{i}.place(x=50+posx,y=180+posy)")

# Establim el focus en la caixa d'entrada ent1
ent1.focus_set()

# Definim una funció que es cridarà quan es premi la tecla Enter
def return_press(event):
    # Si la caixa d'entrada no està desactivada, cridem la funció "calcular"
    if ent1.cget("state") != "disabled":
          calcular()

# Associem la funció return_press a la tecla Enter de la finestra
win.bind("<Return>", return_press)

# Iniciem el bucle principal de la finestra
win.mainloop()