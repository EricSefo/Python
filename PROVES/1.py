llista = []
llista.append(input().split())
strike = int()
contador = int()
while strike != 3:
    for i in llista[0]:
        if i == "-1":
            strike += 1
        else:
            contador += 1
print(contador)