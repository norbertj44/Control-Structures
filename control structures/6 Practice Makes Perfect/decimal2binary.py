decimal_number = int(input("Enter decimal number: "))
binary_number = ""

while decimal_number > 0:
    remainder = decimal_number % 2  #reszta
    binary_number = str(remainder) + binary_number  #dodajemy na lewo od liczby binarnej
    decimal_number = decimal_number // 2  #zaokroglenie '//'

print(f"The binary representation is: {binary_number}")
