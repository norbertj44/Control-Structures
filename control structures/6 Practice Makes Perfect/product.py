current = float(input("Current product price: "))
previous = float(input("Previous product price: "))

price_decrease_percentage = ((previous - current) / previous) * 100

if price_decrease_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {(price_decrease_percentage)}%")

