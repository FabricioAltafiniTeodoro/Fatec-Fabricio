preco01 = float(input("Digite o valor do primeiro numero: "))
preco02 = float(input("Digite o valor do segundo numero: "))

desc1 = preco01 - (preco01 * 0.08)
desc2 = preco02 - (preco02 * 0.11)
soma = desc1 + desc2

print("O valor final da venda foi: ",soma)