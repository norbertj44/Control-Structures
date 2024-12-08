correct_pin = "0805"
attempts = 3

while attempts > 0:
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("PIN code correct! Access granted.")
        break
    else:
        attempts -= 1 #odejmujemy co jedna iteracje 1 (jedna probe)
        print("Incorrect...")
        if attempts == 0:#jesli proby sie wyzeruja to oznacza koniec
            print("Sorry, your payment card has been blocked.")
