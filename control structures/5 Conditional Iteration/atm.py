# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111'  # Initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    print()

    if choice == '1':
        entered_pin = input("Enter your PIN: ")  #
        if entered_pin == pin:  # weryfikacja
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount  #updateujemy balans o wniesiona kwote (depozyt)
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:  # #jesli kwota mniejsza od balansu to:
                balance -= amount  # odejmujemy kwote od balansu
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            entered_pin = input("Enter your PIN: ")  #
            if entered_pin == pin:
                old_pin = input("Enter your old PIN: ")
                if old_pin == pin:  # sprawdzamy czy stary = nowy
                    new_pin = input("Enter your new 4-digit PIN: ")
                    if len(new_pin) == 4 and new_pin.isdigit():  # sprawdzamy czy pin ma 4 wyrazy i czy sa cyframi (isdigit)
                        pin = new_pin  # updateujemy pin
                        print("Your PIN has been successfully changed.")
                    else:
                        print("Invalid PIN. It must be 4 digits.")
                else:
                    print("Incorrect old PIN")  # error jesli stary!=nowy
            else:
                print("Incorrect PIN")  # error jesl zly kod
        elif choice == '5':  # quitujemy jako 5 NIE DZIALA??
            print("Exiting... Thank you for using the ATM!")
            break  # Exit the loop

        else:
            print("Invalid option. Please try again.")