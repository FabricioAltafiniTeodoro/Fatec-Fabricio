print("Lista de numeros")

numeros = [1, 4, 3, 6, 2, 5]

maior = 0

numeros.sort()
for orde in numeros:
        indice = numeros.index(orde)
        numeros[indice] = maior
print(maior)

while numeros > maior:
        maior = numeros.append(numeros)