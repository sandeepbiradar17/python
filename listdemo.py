# data=[10,20,30,40,50]
# # print(data)
# # print(data[0])
# # print(data[1:3])
# # print(data[:3])
# # print(data[2:])
# # print(data[-2:])
# # print(data[:-2])
# for d in data:
#     print(d)

# data.append(90)
# data.append(80)
# print(data)
data=[]
i=1
while(i!=0):
    d=int(input("Enter Number"))
    data.append(d)
    i=int(input("Do you wants to add more?Yes(1)/No(0)"))


print(data)