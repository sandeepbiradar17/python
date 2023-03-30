import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#df=pd.DataFrame(np.random.randn(10/4),index=pd.date_range("01/01/2023",periods=10),list="ABCD")
#df=pd.DataFrame(np.random.randn(10.4),index=pd.Date_range('01/01/2023',periods=10))
#df.plot.bar()
#plt.show()


#df=pd.DataFrame(np.random.randn(10,4),index=pd.date_range("01/01/2023",periods=10))
#df.plot()
#plt.show()
d1=np.random.randn(10,6)
d2=pd.date_range("01/01/2023",periods=10)
print(d1)
print(d2)
df=pd.DataFrame(d1,index=d2,)
df.plot.bar()
plt.show()
