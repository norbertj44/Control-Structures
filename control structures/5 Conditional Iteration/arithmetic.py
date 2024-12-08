###
# Sums numbers entered by user
#
total_sum = 0
count = 0 #liczymy ile razy funkcja iteruje (ile razy wykonuje akcje)

while True:
    number = int(input(f"Enter a number (0 to stop): "))

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count+=1 #kazda akcja to +1 do count

if count > 0:
    mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"Mean: {mean}")
else:
    print("No numbers were entered.")