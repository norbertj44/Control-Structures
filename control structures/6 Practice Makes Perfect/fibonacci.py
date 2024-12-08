a = 0 # bo ciag fibonacciego sie zaczyna od 01
b = 1

for i in range(20):
    print(a, end=" ")  #aby nie robilo nowej lini tylko kontynuowalo
    a, b = b, a + b # kazda kolejna liczba to suma dwoch poprzednich 
