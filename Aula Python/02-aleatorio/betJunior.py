#for i in range(0, 7):
#    print(i)
#print("Fim")  

#for i in range(1, 101, 2):
#    print(i)
#    if i==11:
#        break
#print("Fim")  

#import math
#print(math.sqrt(25)) 


import random

print("-------------------------------------------")
print("                BetJunior                  ")
print("-------------------------------------------")

segredo = random.randrange(1, 11)

#print(segredo)

acertou = False
tentativa = 3

for i in range(1, 4):
    print("Voce possui", tentativa, "tentativas de 3/n")
    numero = int(input("Digite um numero entre 1 e 10: "))

    if numero == segredo:
        acertou = True

    if acertou:
        print("-------------------------------------------")
        print("         Voce acertou!!! parabens          ")
        print("-------------------------------------------")
    else:
        print("voce errou!! tente novamente")
        tentativa -=1
print("Fim de jogo")                   



