total_washing_time = 0

program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')

if program == 'j':
    total_washing_time = 40
elif program == 'u':
    total_washing_time = 70
elif program == 's':
    total_washing_time = 20
else:
    print('Invalid program selection')

extra_rinse = input('Extra rinse? (y/n): ')
extra_spin = input('Extra spin? (y/n): ')

if extra_rinse.lower() == 'y': #.lower czyli obojetne czy duza czy mala literka
    total_washing_time += 15

if extra_spin.lower() == 'y':
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')
