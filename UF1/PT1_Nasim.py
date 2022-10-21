try:
    opcio=int(input("Quina opció vols tria?\n"
                    "Opció 1: Temperatura\n"
                    "Opció 2: Mitjana aritmètica\n"
                    "Opció 3: Pes i altura\n"
                    "Opció 4: Hora i minuts a segons\n"
                    "La teva elecció: "))
except ValueError or NameError:
    print("Introdueix quina opció vols triar.")


    #Temperatura#
try:
    if opcio == 1:
        temperatura=int(input("Dis-me la temperatura en celcius:\n"))
        print ("La temperatura emprada ha sigut "+str(temperatura)+" graus celcius.")
        temperatura=int(temperatura*1.8 + 32)
        print ("La temperatura a Fahrenheit és la següent: "+str(temperatura)+"F.")
except ValueError or NameError:
    print("Introdueix quina opció vols triar.")
    
#Mitjana aritmètica
if opcio == 2:
    a=int(input("Introdueix el primer número: "))
    b=int(input("Introdueix el segon número: "))
    c=((a+b)/2)
    print ("La mitjana aritmètica dels números és: "+str(c))

#Pes i altura
elif opcio == 3:
    a=int(input("Introdueix el teu pes: "))
    b=float(input("Introdueix la teva altura: "))
    c=a/b**2
    print ("Aquest és el teu índex de massa corporal: "+str(c)+".")

#Hora i minuts a segons
elif opcio == 4:
    a=int(input("Introdueix un nombre de hores: "))
    b=int(input("Introdueix un nombre de minuts: "))
    c=a*3600
    d=b*60
    e=c+d
    print("Aquest és la traducció de les hores i minuts introduits a segons: "+str(e)+" segons.")
else:
    print("No has seleccionat cap opció INÚTIL!")