import numpy as np
import pandas as pd
rno=np.array([1,2,3,4,5])
name=np.array(["ajay","amit","jay","sagar","suresh"])
dt=pd.Series(rno,index=[10,11,12,13,14])
dt=pd.Series(rno,index=['a','b','c','d','e'])
print(dt)
print(dt['d'])


st={"Roll NO":rno,"Name":name}
df=pd.DataFrame(st,columns=["Roll NO","Name"])
print(df)