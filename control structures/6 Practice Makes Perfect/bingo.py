for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("BINGO ")  # jesli liczba jest podzielna (0) przez 3 i 5
    elif i % 3 == 0:
        print("THREE ")
    elif i % 5 == 0:
        print("FIVE ")
    else:
        print(i, " ")