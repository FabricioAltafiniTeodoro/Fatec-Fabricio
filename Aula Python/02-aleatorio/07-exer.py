qtd_nota = int(input("Digite a quantidade de notas: "))

i = 1
soma = 0
while i <= qtd_nota:
    nota = float(input("Digite a nota{}: ".format(i)))
    i +=1
    soma = soma + nota

media = soma / i
print("A media da nota é: {} ".format(media))     
