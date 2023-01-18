ar = [0,0,0,0,0,0,0,0,0,0,0]
ar2 = []
acabat = True
while not acabat:
  nota = int(input())
  if nota == -1:
    acabat = True
  elif 0 <= nota <= 10:
    ar2.append(nota)
    ar[nota]+=1
print("ar:",ar)

print("NOTES:",len(ar2),"MITJANA:",(sum(ar2) / len(ar2)),ar)
#,"E:",(ar[9] + ar[10]),"N:",(ar[7] + ar[8]),"B:",ar[6],"S:",ar[5],"I:",(ar[4]),"MD:",(ar[0] + ar[1]+ ar[2]+ ar[3])