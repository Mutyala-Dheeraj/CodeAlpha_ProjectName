# TASK 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "IPHONE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MICROSOFT": 320,
    "AMAZON": 135
}

portfolio = {}
total_investment = 0

# Taking user input
n = int(input("Enter number of stocks you want to buy: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
    else:
        print("Stock not available in price list.")

# Calculating total investment
print("\n----- Portfolio Summary -----")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} -> Price: ${price}, Quantity: {quantity}, Investment: ${investment}")

print(f"\nTotal Investment Value: ${total_investment}")

# Saving result into a text file
file = open("portfolio_summary.txt", "w")

file.write("Portfolio Summary\n")
file.write("---------------------\n")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    file.write(f"{stock} -> Price: ${price}, Quantity: {quantity}, Investment: ${investment}\n")

file.write(f"\nTotal Investment Value: ${total_investment}")

file.close()

print("\nPortfolio summary saved in portfolio_summary.txt")