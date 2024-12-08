# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
switch = input('switch 1 or 2?: ')

if switch == '1':
    light_switch1 = True
    light_switch2 = False
    bulbs = '1 bulb is on'

elif switch == '2':
    light_switch1 = False
    light_switch2 = True
    bulbs = '2 bulbs are on'

else:
    bulbs = 'invalid switch number'

print(bulbs)