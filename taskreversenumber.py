import math
n=int(input("enter the number"))
sum=0
while(n!=0):
    remider=n%10
    sum=remider + sum*10
    n=math.floor(n/10)

print("reverse=" +str(sum))        