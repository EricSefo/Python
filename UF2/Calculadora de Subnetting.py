# Importem el mòdul tkinter.
from tkinter import *
from tkinter import messagebox

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
    
def conversio(p,w,x):
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
        for i in list(map(int ,x.split("."))):
            y = str()
            p += w(i)
            if p.count(".") < 3:
                p += "."
        return p
    
def autocompletar(x,y,z):
    while (x.count("1") + x.count("0")) != y:
        if (x.count("1") + x.count("0")) % 8 == 0 and len(x) > 0:
            x += '.'
        x += z
    return x

classe = str()
tipus = "Pública"
hosts = int()

def calcular():
    a = str()
    b = str()
    masc_binari = str()
    wildcard = str()
    decimal_masc = str()
    count=int()
    ip = str()
    host_max = str()
    broadcast = str()
    xarxa = str()
    host_min = str()
    global classe
    global tipus
    global hosts
    adreça = ent1.get()
    try:
        if adreça.count(".") == 3 and 0 <= int(adreça.split(".")[0]) <= 255 and 0 <= int(adreça.split(".")[1]) <= 255 and 0 <= int(adreça.split(".")[2]) <= 255 and 0 <= int(adreça.split(".")[3]) <= 255:
            a = conversio(a,binari,adreça)
            b = conversio(b,decimal,a)
        else:
            raise ValueError
    except:
        messagebox.showinfo("IP incorrecta", "IP incorrecta")
    try:
        masc = int(ent2.get())
    except:
        messagebox.showinfo("Màscara incorrecta", "Màscara incorrecta")
    if masc >= 0 and masc <= 30:
        masc_binari = autocompletar(masc_binari,masc,"1")
        binari_wildcard = masc_binari.replace("1","0")
        binari_wildcard = autocompletar(binari_wildcard,32,"1")
        masc_binari = autocompletar(masc_binari,32,"0")
    else:
        messagebox.showinfo("Màscara incorrecta", "Màscara incorrecta")
    wildcard = conversio(wildcard,decimal,binari_wildcard)
    decimal_masc = conversio(decimal_masc,decimal,masc_binari)
    for i, c in enumerate(a):
        if c == '1' or c == '0':
            count += 1
            if count == masc:
                ip = a[:i+1]
                hosts = 2**(32 - (ip.count("1") + ip.count("0")))-2
                binari_host_max = autocompletar(ip,31,"1")+"0"
                binari_broadcast = autocompletar(ip,32,"1")
                host_max = conversio(host_max,decimal,binari_host_max)
                broadcast = conversio(broadcast,decimal,binari_broadcast)
                ip = autocompletar(ip,32,"0")
                xarxa = conversio(xarxa,decimal,ip)
    binari_host_min = ip[:-1]+"1"
    host_min = conversio(host_min,decimal,binari_host_min)
    try:
        nova_mascara = int(ent3.get())
        if nova_mascara >= 0 and nova_mascara <= 30 and nova_mascara > masc:
            bits = nova_mascara - masc
            subxarxes_mascara = str(2**bits)
            l22.config(text="Subxarxes de la nova màscara: "+subxarxes_mascara+" subxarxes amb "+str(2**(32-nova_mascara)-2)+" hosts cadascuna")
        else:
            messagebox.showinfo("Màscara nova incorrecta", "Màscara nova incorrecta perquè ha d'estar entre 0 i 30, també ha de ser major que la màscara per defecte.")
    except:
        l22.config(text="")
    try:
        subxarxes_requerides = int(ent4.get())
        if subxarxes_requerides < 1:
            l23.config(text="Es necessiten 0 bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides")
        else:
            for i in range (31-masc):
                subxarxes = 2**i
                if subxarxes_requerides <= subxarxes:
                    l23.config(text="Es necessiten "+str(i)+" bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides. En total es crearan "+str(2**i)+ " subxarxes amb "+str(2**(32-(i+masc))-2)+" hosts cadascuna")
                    break
            if subxarxes_requerides > subxarxes:
                l23.config(text="No hi ha prous bits per obtenir les "+str(subxarxes_requerides)+" subxarxes requerides")
    except:
        l23.config(text="")
    try:
        hosts_requerits = int(ent5.get())
        if hosts_requerits < 1:
            l24.config(text="Es necessiten 0 bits per obtenir els "+str(hosts_requerits)+" hosts requerits")
        else:
            for i in range (32-masc):
                hosts_subxarxa = (2**i)-2
                if hosts_requerits <= hosts_subxarxa:
                    print("A",hosts_requerits,hosts_subxarxa)
                    l24.config(text="Es necessiten "+str(i)+" bits per obtenir els "+str(hosts_requerits)+" hosts requerits en "+str(2**(32-(i+masc)))+" subxarxes amb "+str(hosts_subxarxa)+" hosts per subxarxa en total")
                    break
            if hosts_requerits > hosts_subxarxa:
                l24.config(text="No hi ha prous bits per obtenir els "+str(hosts_requerits)+" hosts requerits")
    except:
        l24.config(text="")
    
    if 0 <= int(b.split(".")[0]) <= 127 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 10 == int(b.split(".")[0]) and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada"
        classe = "Classe A"
    elif 128 <= int(b.split(".")[0]) <= 191 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 172 == int(b.split(".")[0]) and 16 <= int(b.split(".")[1]) <= 31 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada"
        classe = "Classe B"
    elif 192 <= int(b.split(".")[0]) <= 223 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        if 192 == int(b.split(".")[0]) and 168 == int(b.split(".")[1]) and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
            tipus = "Privada"
        classe = "Classe C"
    elif 224 <= int(b.split(".")[0]) <= 239 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        classe = "Classe D"
    elif 240 <= int(b.split(".")[0]) <= 255 and 0 <= int(b.split(".")[1]) <= 255 and 0 <= int(b.split(".")[2]) <= 255 and 0 <= int(b.split(".")[3]) <= 255:
        classe = "Classe E"
    else:
        messagebox.showinfo("IP incorrecta", "IP incorrecta",ip,b)
    l6.config(text="Adreça: "+b)
    l7.config(text=a)
    l8.config(text="Màscara: "+decimal_masc+" = "+(str(masc)))
    l9.config(text=masc_binari,fg="red")
    l10.config(text="Màscara Wildcard: "+wildcard)
    l11.config(text=binari_wildcard)
    l12.config(text="Xarxa: "+xarxa)
    l13.config(text=ip)
    l14.config(text="Host Mínim: "+host_min)
    l15.config(text=binari_host_min)
    l16.config(text="Host Màxim: "+host_max)
    l17.config(text=binari_host_max)
    l18.config(text="Broadcast: "+broadcast)
    l19.config(text=binari_broadcast)
    l20.config(text="Hosts per xarxa: "+str(hosts))
    l21.config(text=classe+", "+tipus)

def clear():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)
    ent4.delete(0,END)
    ent5.delete(0,END)
    for i in range (6,25):
        exec(f"l{i}.config(text='')")
    
win = Tk() #Creem una finestra principal per a l'aplicació
win.geometry("1500x600") #Establim la mida de la finestra
win.configure(bg = '#e8e4e4') #Establim el color de fons de la finestra
win.title('Calculadora IP') #Establim el títol de la finestra

l0 = Label(text="Calculadora IP", fg="blue", bg="#e8e4e4",border=15, font=("Arial", 25, "bold"))
l0.place(x=580,y=0)

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
btn1 = Button(text="Calcular", command=calcular, font=("Arial", 12), bg="#e8e4e4") 
btn1.place(x=50,y=130)
btn2 = Button(text="Llimpiar", command=clear, font=("Arial", 12), bg="#e8e4e4") 
btn2.place(x=130,y=130)

posy = int()
for i in range (6,25):
    posx = int()
    if i > 22:
        posx = 0
        posy += 20
    else:
        if i % 2 != 0:
            posx += 280
        else:
            posy += 20
    exec(f"l{i} = Label(font=('Arial', 12, 'bold'), fg='black', bg='#e8e4e4')")
    exec(f"l{i}.place(x=50+posx,y=180+posy)")
ent1.focus_set()
def return_press(event):
    if ent1.cget("state") != "disabled":
          calcular()
win.bind("<Return>", return_press)
win.mainloop()