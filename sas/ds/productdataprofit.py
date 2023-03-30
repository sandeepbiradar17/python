import pandas as pd
from matplotlib import pyplot as plt
st={"Product":["Pen","pencil","sugar","soap","Pen","pencil","sugar","soap","Pen","pencil","sugar","soap","Pen","pencil","sugar","soap"],
"year":[2010,2010,2010,2010,2011,2011,2011,2011,2012,2012,2012,2012,2013,2013,2013,2013],
"profit":[10000,2300,5700,6000,10000,23600,57300,61000,105000,23500,57500,62000,100000,23000,57000,6000]}
df=pd.DataFrame(st)
#print(df)

data=df.groupby(["year","profit"])
for group,dt in data:
    print(group)
    print(dt)
#Product_profit=df.groupby("Product")['profit'].sum()

#print(Product_profit)
#yearly_product_profit=df.groupby(['year','Product'])['profit'].sum()
#print(yearly_product_profit)
#df.pd.DataFrame(st)
#df.plot(kind='bar',x='year',y='profit',color='red')
# plt.title('Bar plot')
#plt.show()


# product=str(input("enter product name:"))
# pencil_df=df[df["Product"]==product]

#print(f"The profit of {product} for year {year} is {profit}")
#pencil_df.plot(kind='bar',x='year',y='profit',color='red')   
# plt.plot(pencil_df["year"],pencil_df["profit"])
#df.plot(kind='bar',x='year',y='profit',color='red')

#plt.bar(x,y)
# plt.xlabel("year")
# plt.ylabel("profit")
#plt.show()

# product=input("enter product name:")
pencil_df=df[df["Product"]== product]
# plt.plot(pencil_df["year"],pencil_df["profit"])

# plt.show()
