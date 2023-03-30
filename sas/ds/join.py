import pandas as pd

student={"rno":[1,2,3,4,5,6,7],"name":["ajay","amit","sagar","suraj","dinesh","deepak","amay"]}
studentsubjects={"rno":[1,3,5,7,9,10,8],"subject":["English","maths","science","Hindi","history","Python","java"]}
left=pd.DataFrame(student)
right=pd.DataFrame(studentsubjects)
print(left)
print(right)

# data1=pd.merge(left,right,on="rno")
# data2=pd.merge(left,right,on="rno",how="right")
# data3=pd.merge(left,right,on="rno",how="left")
# data4=pd.merge(left,right,on="rno",how="outer")

# print(data1)
# print(data2)
# print(data3)
# print(data4)