pesos = {'Pepe':[56, 64, 54],'Paco':[89, 87, 86], 'Pancracio':[102, 105, 111]}

usr=input("Introdueix un Usuari:")
pes=int(input("Introdueix un pes:"))
try:
 pesos[usr].append(pes)
except KeyError:
 pesos[usr]=[pes]

print("Pesos de ",usr,pesos[usr]);

#print (diccionari['Paco'])
#print (len(diccionari))
#print ('Pancracio' in diccionari)
#d={'a':2,'b':56,'c':1434}
#valors = list(d.values())
#x=int(input("Valor a cercar: "))
#print (x in valors)
