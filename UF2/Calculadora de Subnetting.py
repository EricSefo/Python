# Importem el mòdul tkinter.
from tkinter import *

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
    
def autocompletar(x,y,z):
    while (x.count("1") + x.count("0")) != y:
        if (x.count("1") + x.count("0")) % 8 == 0 and len(x) > 0:
            x += '.'
        x += z
    return x

a = str()
b = str()
a = conversio(a,binari)
b = conversio(b,decimal,a)

masc = int(input("Màscara de xarxa: "))
if masc >= 0 and masc <= 32:
    masc_binari = str()
    masc_binari = autocompletar(masc_binari,masc,"1")
    masc_binari = autocompletar(masc_binari,32,"0")
else:
    print("Màscara incorrecta")
    exit()
     
decimal_masc = str()
decimal_masc = conversio(decimal_masc,decimal,masc_binari)
tipus = "Pública"

count=int()
for i, c in enumerate(a):
    if c == '1' or c == '0':
        count += 1
        if count == masc:
            ip = a[:i+1]
            hosts = 2**(32 -(ip.count("1") + ip.count("0")))-2
            host_max = str()
            broadcast = str()
            host_max = conversio(host_max,decimal,(autocompletar(ip,31,"1")+"0"))
            broadcast = conversio(broadcast,decimal,(autocompletar(ip,32,"1")))
            ip = autocompletar(ip,32,"0")
            xarxa = str()
            xarxa = conversio(xarxa,decimal,ip)
ip = ip[:-1]+"1"
host_min = str()
host_min = conversio(host_min,decimal,ip)
classe = str()

def calcular():
    global classe
    global tipus
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
        print("IP incorrecta")
        exit()
print(b,a,classe,tipus,masc_binari,masc,decimal_masc,ip,xarxa,host_min,host_max,broadcast,hosts)

win = Tk() #Creem una finestra principal per a l'aplicació
win.geometry("1366x768") #Establim la mida de la finestra
win.configure(bg = '#e8e4e4') #Establim el color de fons de la finestra
win.title('Calculadora IP') #Establim el títol de la finestra

l0 = Label(text="Calculadora IP", fg="blue", bg="#e8e4e4",border=15, font=("Arial", 20, "bold")) #Creem una etiqueta per mostrar el títol de l'aplicació
l0.place(x=580,y=0)

l1 = Label(text="Adreça (Host o Xarxa):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4") #Creem una etiqueta per mostrar la paraula endevinada o les lletres endevinades
l1.place(x=47,y=70)
ent1 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent1.place(x=50,y=100)

l2 = Label(text="Màscara:", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4") #Creem una etiqueta per mostrar la paraula endevinada o les lletres endevinades
l2.place(x=247,y=70)
ent2 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent2.place(x=250,y=100)

l3 = Label(text="Màscara per subxarxa (opcional):", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4") #Creem una etiqueta per mostrar la paraula endevinada o les lletres endevinades
l3.place(x=447,y=70)
l4 = Label(text="moure a:", font=("Arial", 12, "bold"), fg="black", bg="#e8e4e4") #Creem una etiqueta per mostrar la paraula endevinada o les lletres endevinades
l4.place(x=447,y=100)
ent3 = Entry(font=("Arial", 12, "bold"), fg="black", bg="white")
ent3.place(x=525,y=100)

btn1 = Button(text="Calcular", command=None, font=("Arial", 12), bg="#e8e4e4") 
btn1.place(x=50,y=130)

btn2 = Button(text="Llimpiar", command=None, font=("Arial", 12), bg="#e8e4e4") 
btn2.place(x=130,y=130)

ent1.focus_set()
def return_press(event):
      if ent1.cget("state") != "disabled":
            None
win.bind("<Return>", return_press)
win.mainloop()