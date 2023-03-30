# # # import pandas as pd
# # # import numpy as np
# # # from matplotlib import pyplot as plt

# # # # Define the student data and subject scores
# # # student = {"rno": [1,2,3,4,5,6]}
# # # studentsubjects = {"english": [90,34,35,67,34,50],
# # #                    "maths": [23,45,29,45,34,65],
# # #                    "science": [78,34,26,67,34,50]}

# # # # Create a DataFrame from the data
# # # df = pd.DataFrame(studentsubjects, index=student["rno"])

# # # # Plot the data
# # # df.plot(kind="bar")

# # # # Add labels and title
# # # plt.xlabel("Roll Number")
# # # plt.ylabel("Marks")
# # # plt.title("Subject Scores for Each Student")

# # # # Display the graph
# # # plt.show()
# # # print(student)
# # # print(studentsubjects)

# # import pandas as pd
# # import numpy as np
# # from matplotlib import pyplot as plt

# # # Define the student data and subject scores
# # student = {"rno": [1,2,3,4,5,6]}
# # studentsubjects = {"english": [90,34,35,67,34,50],
# #                    "maths": [23,45,29,45,34,65],
# #                    "science": [78,34,26,67,34,50]}

# # # Create a DataFrame from the data
# # df = pd.DataFrame(studentsubjects, index=student["rno"])

# # # Plot the data
# # df.plot(kind="bar")

# # # Add labels and title
# # plt.xlabel("Roll Number")
# # plt.ylabel("Marks")
# # plt.title("Subject Scores for Each Student")

# # # Display the graph
# # plt.show()

# # # Print the student data and subject scores
# # print(student)
# # print(studentsubjects)

# import pandas as pd
# import matplotlib.pyplot as plt

# # Define the data
# st={"Product":["pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt"],
# "Year":[2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013],
# "profit":[20,30,40,50,50,40,30,20,100,150,160,180,200,220,250,260]}

# # Create the DataFrame
# df=pd.DataFrame(st)

# # Group by product and year to get the profit of each product in each year
# yearly_product_profit=df.groupby(['Year','Product'])['profit'].sum()

# # Get user input for the year
# year=int(input("Enter year: "))

# # Filter the DataFrame to get data for the specified year
# year_df = yearly_product_profit.loc[year]

# # Create a bar chart
# plt.bar(year_df.index.get_level_values(1), year_df.values)
# plt.xlabel('Product')
# plt.ylabel('Profit')
# plt.title(f'Product Profit in {year}')
# plt.show()
import pandas as pd
from matplotlib import pyplot as plt

st={"Product":["pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt","pen","pencil","sugar","salt"],
"Year":[2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013,2010,2011,2012,2013],
"profit":[20,30,40,50,50,40,30,20,100,150,160,180,200,220,250,260]
}

df=pd.DataFrame(st)
print(df)

# group by Year and profit
data=df.groupby(["Year","profit"])
for group,dt in data:
    print(group)
    print(dt)

# group by Product and sum the profits
Product_profit=df.groupby("Product")['profit'].sum()
print(Product_profit)

# group by Year and Product and sum the profits
yearly_product_profit=df.groupby(['Year','Product'])['profit'].sum()
print(yearly_product_profit)

# get profits for a specific year
Year=int(input("enter year name:"))
year_data=df[df["Year"]==Year]
print(year_data)

# plot yearly profits by product
yearly_product_profit.unstack().plot(kind='bar')
plt.show()
