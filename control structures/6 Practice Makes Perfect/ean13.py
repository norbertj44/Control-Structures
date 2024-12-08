ean_number = input("Enter EAN-13 article number: ")

if len(ean_number) == 13 and ean_number.isdigit(): #czy liczba numeru to 13 i czy sa to tylko cyfry (.isdigit)
    print("Article number is correct")

    if ean_number.startswith("590"): #startswith - czy zaczyna sie na
        print("Article manufactured in Poland")
else:
    print("Invalid EAN-13 article number")
