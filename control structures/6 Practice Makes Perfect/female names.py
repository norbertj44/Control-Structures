name = input("enter name: ")

if name[-1].lower() == 'a':  #.lower czyli jak wpiszemy nawet z duzej to nie wypluje bledu i -1 bo od konca
    print(f"{name} -> polish female name")
else:
    print(f"{name} -> not a polish female name")
