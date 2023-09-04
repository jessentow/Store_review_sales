# Azubi store information

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculation of the total price average for all products
Sum_of_total_price = sum(prices)
average_price = Sum_of_total_price / len(prices)
a = f"{average_price:.2f}"
print("Average Price:", a)

# Creation of  a new price list that reduces the old prices by $5
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# Calculation of  the total revenue generated from the products
total_revenue = sum(prices[i] * last_week[i] for i in range(len(products)))
print("Total Revenue:", total_revenue)

# Calculation of  the average daily revenue generated from the products
average_daily_revenue = total_revenue / sum(last_week)
b  = f"{average_daily_revenue:.2f}"
print("Average Daily Revenue:", b)

# Based on the new prices, which products are less than $30
products_less_than_30 = [products[i] for i in range(len(products)) if new_prices[i] < 30]
print("Products less than $30 :", products_less_than_30)
