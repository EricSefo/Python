def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
        resultado=n+factorial(n-1)
   return resultado

paco=int(input())
while paco > 0:
    paco2=int(input())
    variable = int()
    for i in range(paco2):
        fact=factorial(paco2)
        paco2 -= 1
        variable += fact
    print(variable)
    paco -= 1