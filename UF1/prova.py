pesos = {'Pepe':[56, 64, 54],'Paco':[89, 87, 86], 'Pancracio':[102, 105, 111]}

try:
    usr=input("Introdueix el nom d'un Usuari: ")
    pes=float(input("Introdueix un pes en kg: "))
    pesos[usr].append(pes)
    print("Pesos de",usr,pesos[usr]);
except KeyError:
    pesos[usr]=[pes]
    print("Pesos de",usr,pesos[usr]);  
except ValueError:
    print("Introdueix el pes en números")
    
#print (diccionari['Paco'])
#print (len(diccionari))
#print ('Pancracio' in diccionari)
#d={'a':2,'b':56,'c':1434}
#valors = list(d.values())
#x=int(input("Valor a cercar: "))
#print (x in valors)