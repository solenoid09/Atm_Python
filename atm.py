withdrawn,balance = input().split()
withd = int(withdrawn)
bal = float(balance)
if (withd%5 ==0 and 0<withd<=bal-0.5):
    print ("%.2f"%(bal - (withd +0.5)))
else:
    print ("%.2f"%bal)
