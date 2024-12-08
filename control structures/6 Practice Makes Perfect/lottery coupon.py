for i in range(1, 8):
    for j in range(i, 50, 7): #robimy 2 for'y w jednym, bo kolumny to 1 do 8 (pierwszy for) a liczby w nich to 1-7 od pionu do liczby 49
        print(j, end=" ")
    print()  # przesuwamy sie do nastepnej linijki po rzedzie
