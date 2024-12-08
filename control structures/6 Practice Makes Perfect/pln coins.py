amount = int(input("enter the amount in PLN: "))

five_pln = amount // 5
amount %= 5 #to samo co amount = amount % 5 (czyli reszta z dzielenia przez 5)

two_pln = amount // 2
amount %= 2

one_pln = amount

# Print the result
print(f"The amount of PLN {amount} in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")
