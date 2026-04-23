nome = str(input("Digite o seu nome: "))
nota1 = float(input("Digite a sua nota1: "))
nota2 = float(input("Digite a sua nota2: "))
nota3 = float(input("Digite a sua nota3: "))

media = (nota1 + nota2 +nota3)/3

if media > 7:
    print("Parabens {}! Voce foi Aprovado".format(nome))
elif media < 7 and media > 5:
    print("Voce foi com media {} e esta de recuperacao".format(media))
else:
    print("{} voce esta reprovado".format(nome))       

        