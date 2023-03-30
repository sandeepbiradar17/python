import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
rno=([1,2,3,4,5,6,7])
name=np.array(["ajay","mumbai","pune","solapur","nagpur","thane","bhiwandi"])
pen=[60,70,80,90,100,50,20]
pencil=[20,50,100,90,80,70,60]
sugar=[100,90,20,50,60,70,80]
salt=[70,50,10,60,70,60,80]
st={"Rno":rno,"Name":name,"Pen":pen,"Pencil":pencil,"Sugar":sugar,"Salt":salt}

#df=pd.DataFrame(st,columns=["RNO NO","Name","English","Maths","Science"])
df=pd.DataFrame(st,columns=["Rno","Name","Pen","Pencil","Sugar","Salt"])
print(df)
df["Total"]=df["Pen"]+df["Pencil"]+df["Sugar"]+df["Salt"]
df["Percentage"]=df["Total"]/4
df["Result"]=df["Percentage"].apply(lambda p:'pass' if  p>=40 else "Fail")
print(df)

df.to_excel("sandeep.xlsx")
df.to_csv("sandeep.csv")

df.plot(x="Rno",y="Percentage",kind="bar")

plt.show()

