#Temperatura#
temperatura=int(input("Dis-me la temperatura en celcius:\n"))
print ("La temperatura emprada ha sigut "+str(temperatura)+" graus celcius.")
temperatura=int(temperatura*1.8 + 32)
print ("La temperatura a Fahrenheit és la següent: "+str(temperatura)+"F.")

#Mitjana aritmètica
a=int(input("Introdueix el primer número: "))
b=int(input("Introdueix el segon número: "))
c=((a+b)/2)
print ("La mitjana aritmètica dels números és: "+str(c))

#Pes i altura
a=int(input("Introdueix el teu pes: "))
b=float(input("Introdueix la teva altura: "))
c=a/b**2
print ("Aquest és el teu índex de massa corporal: "+str(c)+".")

#Hora i minuts a segons
a=int(input("Introdueix un nombre de hores: "))
b=int(input("Introdueix un nombre de minuts: "))
c=a*3600
d=b*60
e=c+d
print("Aquest és la traducció de les hores i minuts introduits a segons: "+str(e)+" segons.")
