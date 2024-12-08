num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if num_products > 2:
    discount = 0.25
else:
    discount = 0

total_price = num_products * product_price
discounted_price = total_price * (1 - discount)

print(f"Amount to pay: {discounted_price}")
