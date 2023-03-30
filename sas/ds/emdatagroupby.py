import pandas as pd
st={"employee_id":[1,2,3,4,5,6,7,8,9,10,11,12,13],"employee_name":["Amit","ajay","jay","sanjay","rajesh","sagar","suresh","deepak","Jaydeep","Akash","Akshay","ashok","Dinesh"],"designation":["tester","developer","Accountant","tester","Accountant","developer","tester","Accountant","Accountant","Accountant","tester","tester","tester"]}
df=pd.DataFrame(st)
#print(df)
data=df.groupby("designation")
#print(data)
#data=df.groupby("designation")
print(data)
#print(data.get_group("tester"))
#for d in data:
 #   print(d)

for group,dt in data:
    print(group)
    print(dt)