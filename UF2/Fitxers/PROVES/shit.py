cont = 0
k = list(map(int, input().split()))
for i in k:
    if i <= 30:
        cont += 1
print(cont)