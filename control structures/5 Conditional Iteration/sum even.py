###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
i=1 #bo musimy zaczac liczenie od 1

# Calculate the sum of even numbers
while i <= N: #jak dojdzie do N (czyli 10) to sie zatrzyma)
    if i % 2 == 0: #dla liczb parzystych
        sum_even += i #jak parzysta to dodajemy do sumy
    i += 1 # po kazdej liczbie zwiekszamy iteracje o 1 zeby przejsc do nastepnej liczby

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")