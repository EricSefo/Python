import random
num = random.randint(0,100)
contador = 5
while contador > 0:
    try:
        candidat=int(input("Adivina el número enter entre 0 i 100: "))  
        if candidat < 0 or candidat > 100:
            print("Introdueix un número enter entre el 0 i el 100")
        elif num > candidat:
            print("El número és més mejor a",candidat)
        elif num < candidat:
            print("El número és més menor a",candidat)
        elif num == candidat:
            print("Has acertat el número!")
            break
        
    except ValueError:
        print("Introdueix un número enter entre el 0 i el 100")
    except:
        print("S'ha produit un error")  
    contador -= 1
    
if contador == 0:
    print("S'han acabat els intents")

pesos = {'Pepe':[56.6, 64.3, 54.1],
         'Paco':[89.4, 87.3, 86.5], 
         'Pancracio':[102.8, 105.7, 111.9]}

try:
    usr=input("Introdueix el nom d'un Usuari: ")
    pes=float(input("Introdueix un pes en kg: "))
    pesos[usr].append(pes)
    print("Pesos de",usr,pesos[usr])
except KeyError:
    pesos[usr]=[pes]
    print("Pesos de",usr,pesos[usr])
except ValueError:
    print("Introdueix el pes en números")
except:
    print("S'ha produit un error") 
# Versió 1 poc eficient
'''i=0
pesos[usr]
while i<len(pesos[usr]):
    print(pesos[usr][i])
    i+=1'''

# Versió 2

pes_antic = 0
for pes in pesos[usr]:
    if pes_antic!=0:
     diferencia = pes - pes_antic
     print(round(diferencia,2))    
 
    pes_antic = pes
