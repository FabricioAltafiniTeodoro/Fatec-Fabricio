numeros = [10, 11, 12, 13, 14, 15, 16]
num = int(input("Digite um numero entre 10 e 16: "))

if num in numeros:
        indice = numeros.index(num)
        numeros[indice] = 7
        print(numeros)
else:
        print("Numero Invalidao")    