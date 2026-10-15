# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data

# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format
with open("sales.csv", "r") as file:
    content = file.read()
lines = content.splitlines()
headers = lines[0].split(",")

sales = []

for line in lines[1:]:
    values = line.split(",")
    sales.append(values)

largest_sale = max(sales, key=lambda row: float(row[2]))

total_sales = sum(float(row[2]) for row in sales)
average_sales = total_sales / len(sales)

widget_sales = {}

for row in sales:
    product = row[1]
    units = int(row[3])

    if product in widget_sales:
        widget_sales[product] += units
    else:
        widget_sales[product] = units
best_widget = max(widget_sales, key=widget_sales.get)

print("SALES REPORT")
print("-" * 30)
print(f"Largest sale day: {largest_sale[0]}")
print(f"Product: {largest_sale[1]}")
print(f"Sales amount: £{float(largest_sale[2]):,.2f}")
print(f"Average sale amount: £{average_sales:,.2f}")
print(f"Best-selling widget: {best_widget}")
print(f"Total units sold: {widget_sales[best_widget]}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows