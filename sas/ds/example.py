import pandas as pd
from matplotlib import pyplot as plt
import pandas as pd
st={"Product":["pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt"],
"Year":[2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013],
"profit":[20,30,40,50,50,40,30,20,100,150,160,180,200,220,250,260]
}
df=pd.DataFrame(st)

print(df)

data=df.groupby(["Year","profit"])
for group,dt in data:
    print(group)
    print(dt)
Product_profit=df.groupby("Product")['profit'].sum()

print(Product_profit)

yearly_product_profit=df.groupby(['Year','Product'])['profit'].sum()
print(yearly_product_profit)

Year=int(input("enter year name:"))
Yeasr=df[df["Year"]==Year] 
print(Yeasr)


yearly_product_profit.unstack().plot(kind='bar')

plt.show()