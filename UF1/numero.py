import time
num=67


candidat=int(input("Escull un número entre 0 i 100: "))
while True: 
    if num > candidat:
        print("El número és més mejor a ",candidat)
    elif num < candidat:
        print("El número és més menor a",candidat)
    elif num == candidat:
        print("Has acertat el número!")
    else: 
        print("Torna-ho a intentar...")
    time.sleep(5)
