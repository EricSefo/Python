n = int(input())
a = 0
while True:
    a += 1
    if n < 0:
        z = "mati del dia"
        break
    if n >= 43200:
        z = "nit del dia"
        break
    n -= 43200
print(z,a)