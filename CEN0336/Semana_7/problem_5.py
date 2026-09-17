#Script de cálculo do fatorial de 1000
n = 1000
fat = 1
contador = n

while contador > 1:
    fat = fat * contador
    contador = contador - 1

print(fat)
