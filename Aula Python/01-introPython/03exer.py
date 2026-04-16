nome = str(input("Digite o seu nome: "))
nota1 = int(input("Digite nota 01: "))
nota2 = int(input("Digite nota 02: "))

media = ( nota1 + nota2)/2

if media >=7:
    print("Parabens{}! Voce foi aprovado".format(nome))
else:
    print("Voce ficou com media {} e foi reprovado".format(media))
