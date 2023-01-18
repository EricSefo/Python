hores = int(input())
minuts = int(input())
minuts_durada = int(input())
if hores >= 0 and hores <= 23 and minuts >= 0 and hores <= 59:
    '''if minuts_durada > 60:
       minuts_durada = minuts_durada * 60
       hores = hores / 3600
       minuts = minuts / 60
       temps = minuts_durada - hores + minuts
       temps = temps // 3600
       decimals = 0.7 * 60
       print (str(int(temps))+(":")+str(int(decimals)))
    minuts_durada = minuts_durada % 60'''
    if minuts_durada < 60:
        hores += 1
        minuts += minuts_durada-60
        print (str(hores)+(":")+str(minuts))