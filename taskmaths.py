import math
n=int(input("enter any number"))
count=0
while(n!=0):
    count=count+1
    n=math.floor(n/10)

print("total digits="+str(count))