x = int(input("enter x coordinate: "))
y = int(input("enter y coordinate: "))

if x == 0 and y == 0:
    print("Point P(0,0) is at the origin")
elif x == 0:
    print(f"Point P({x},{y}) is on the y-axis")
elif y == 0:
    print(f"Point P({x},{y}) is on the x-axis")
elif x > 0 and y > 0:
    print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
else:
    print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system") # x > 0 i y < 0
