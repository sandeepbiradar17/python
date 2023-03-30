import matplotlib.pyplot as plt
products = {
    "apple": [1000, 2000, 3000, 4000],
    "banana": [10000,4000, 5000, 1000],
    "orange": [4000, 5000, 6000, 7000],
    "mango": [2000, 3000, 4000, 5000]}


product_name = input("Enter a product name: ")


if product_name in products:
     #get the profits of the input product name for multiple years
    profits = products[product_name]
    
    #print the profits of the input product name for multiple years
    for i, profit in enumerate(profits):
        year = i + 1
    print(f"The profit of {product_name} for year {year} is {profit}")
    
    #plot the profits in a bar chart
    years = [i+1 for i in range(len(profits))]
    plt.bar(years, profits)
    plt.title(f"{product_name.capitalize()} Profit for Multiple Years")
    plt.xlabel("Year")
    plt.ylabel("Profit")
    plt.show()
else:
    print("Product not found!")