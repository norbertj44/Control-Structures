hours = int(input("enter the number of hours the car was parked: "))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0  

print(f"the parking fee for {hours} hours is {fee} PLN.")
