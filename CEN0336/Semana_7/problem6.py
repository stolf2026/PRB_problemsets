#Iterando pelos elementos de uma lista
numeros = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]

for n in numeros:
    if n % 2 == 0:
        print(n, "é par")
    else:
        print(n, "é ímpar")
