###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print('it is extremely hot')
elif temperature >= 15:
    print('it is hot')
elif temperature >= 0:
    print('it is warm')
elif temperature < 0:
    print('Warning, frost')
