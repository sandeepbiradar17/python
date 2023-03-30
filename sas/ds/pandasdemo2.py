import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
rno=np.array([1,2,3,4,5,6])
name=np.array(["ajay","amit","jay","sagar","suraj","sanjay"])
english=[90,34,35,67,34,50]
maths=[23,45,29,45,34,65]
science=[78,34,26,67,34,50]
st={"RNO NO":rno,"Name":name,"English":english,"Maths":maths,"Science":science}

df=pd.DataFrame(st,columns=["RNO NO","Name","English","Maths","Science"])
print(df)
df["Total"]=df["English"]+df["Maths"]+df["Science"]
df["Percentage"]=df["Total"]/3
df["Result"]=df["Percentage"].apply(lambda p:'pass' if  p>=40 else "Fail")
print(df)

df.to_excel("student.xlsx")
df.to_csv("student.csv")

df.plot(x="RNO NO",y="Percentage",kind="bar")

plt.show()