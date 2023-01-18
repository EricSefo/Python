#Exercici 1

h=int(input("Hora inici:"))
m=int(input("Minurs inici:"))
d=int(input("Durada esdeveniment"))

#Calcul dels minuts totals de duraciÃ³ comptant les hores i minuts
md=m+d(h*60);
print("Minuts final:",md);

#Passem els minuts totals de durada a hores amb la divisiÃ³ entera
hd=md//60;
hd=hd%24;

#Obviem les hores i dies calculats i ens centrem amb el modul que se
md=md%60;

print("Hora de finalitzaciÃ³:",str(hd)+":"+str(md));

#Exercici 2
secret=777;

while(True):
    usr=int(input("Tria un nÃºmero: "))
    if(usr!=secret):
        print("Ha, ha! EstÃ s atrapat al meu bucle!")
    else:
        print("Has escollit",usr,"Ben fet, muggle! Ets lliure ara")
        break

#Exercici 3
my_list=[1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list.sort() #Sort es pa ordenar
llista=[]
pivot='';
for x in my_list:
    if x !=pivot:
        llista.append(x) #Pa afegir element a llista
        pivot=x;

print("La llista amb elements Ãºnics:")
print(llista)