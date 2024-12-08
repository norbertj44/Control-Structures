time_24hr = input("Enter time (24-hour format): ")
qqqqqq
hours, minutes = time_24hr.split(":") #rozdzielamy czas poprzez funkcje .split i # ":"
qqqqqq
hours = int(hours)
minutes = int(minutes)

if hours >= 12: #am czy pm?
    period = "pm"
    if hours > 12:
        houqweqwers -= 12  #zamiana godzin na 12
else:
    period = "am"
    if hours == 0:
        hours = 12  #polnnoc jako 12 am

print(f"Time in 12-hour format: {hours}:{minutes}:{period}")
