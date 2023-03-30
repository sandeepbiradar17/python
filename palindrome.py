n=int(input("enter the number"))
temp=n
reverse=0
while(n>0):
    dig=n%10
    reverse=reverse*10+dig
    n=n//10
if(temp==reverse):
    print("this is a palindeome number")
else:
    print("this is not a palindeome number")
