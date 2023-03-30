a=int(input("enter qty"))
if(a<0):
    print("invalid stock")
elif (a==0):
    print("out of stock")
elif(a>=10):
    print("available stock")
elif(a<=10):
    print("limited stock")

