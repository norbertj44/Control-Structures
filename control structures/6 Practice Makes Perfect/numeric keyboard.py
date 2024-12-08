#for i in range(6,-1,-3):
    #for j in range(1,4):
        #print(f'{i+j}',end=' ')
    #print()


i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f'{i + j}', end=' ') #nie dodajemy nowej lini jak klawiatura numeryczna
        j += 1
    print() #przechodzimy do nastepnego wierszu
    i -= 3
