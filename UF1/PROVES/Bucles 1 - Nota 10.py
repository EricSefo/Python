notes10 = int()
notes = int()
while True:
    x = int(input())
    if x == -1:
        break
    elif x == 10:
        notes10 += 1; notes += 1; 
    elif x >= 0 and x <= 10:
        notes += 1
print ("TOTAL NOTES: ",notes,"NOTES10: ",notes10)