#Tasca1:
#Escriu un programa que sol·liciti una puntuació entre 0 i 10. 
# Si la puntuació és fora d'aquest rang, mostra un missatge d'error. 
# Si la puntuació està entre 0 i 10, mostra la qualificació usant la taula següent:
#Puntuació Qualificació
# >= 9 Excel·lent >= 8 Notable >= 7 Bé >= 5 Suficient < 5 Insuficient
#Bateria de proves: Introduïu puntuació: 9.5 -> Excel·lent Introduïu puntuació: perfecte -> Puntuació incorrecta
#Introduïu puntuació: 11 Puntuació -> Incorrecta, Introduïu puntuació: 7.5 -> Bé. Introduïu puntuació: 0.5 -> Insuficient
try:
    puntuacio=float(input("Introdueix una puntuació entre 0 i 10: "))
    if puntuacio > 10 or puntuacio < 0:
        print("Incorrecta")
    elif puntuacio >= 9:
        print("Excel·lent")
    elif puntuacio >= 8:
        print("Notable")
    elif puntuacio >= 7:
        print("Bé.")
    elif puntuacio >= 5:
        print("Suficient")
    elif puntuacio < 5:
        print("Insuficient")
except ValueError:
    print("Puntuació incorrecta")
#Tasca 2:
#Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
#Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.s
try:
    any_actual=int(input("En quin any estem actualment: "))
    any_random=int(input("Dis-me un any qualsevol: "))
    diferencia= abs(any_actual - any_random)
    if any_actual > any_random and diferencia != 1:
        print("Han passat",str(diferencia),"anys")
    elif any_actual < any_random and diferencia != 1:
        print("Falten",str(diferencia),"anys")
    elif diferencia == 1 and any_random > any_actual:
        print("Només falta un any")
    elif diferencia == 1 and any_random < any_actual:
        print("Ha passat un any")
    else:
        print("No hi ha diferència perquè són iguals")
except ValueError:
    print("Introdueix l'any correctament")

#Tasca 3:
#Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
#Podeu utilitzar la funció randint() de la llibreria random:
#Exemple d'ús:
import random
numero = random.randint(1, 6)

try:
    tirada=input("Tira el dau introduint la paraula 'tirar': ")
    if (tirada == "tirar"):
        print("Has tret el número:",numero)
    else:
        print("Has d'introduir la paraula 'tirar' per jugar")
except ValueError:
    print("Paraula o caràcter incorrect/a")