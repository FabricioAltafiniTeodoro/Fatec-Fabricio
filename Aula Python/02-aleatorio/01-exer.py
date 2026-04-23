import os
import random

print("-------------------------------------------")
print("                BetJunior                  ")
print("-------------------------------------------")

segredo = random.randrange(1, 11)

def limpar_tela():
   
    os.system('cls' if os.name == 'nt' else 'clear')

#print(segredo)

tentativa = 3
recomeco = "s"
i = 1
if recomeco == "s":
    i -=1
    for i in range(1, 4):
    
            print("Voce possui", tentativa, "tentativas")
            numero = int(input("Digite um numero entre 1 e 10: "))
            limpar_tela()

            if numero >= 1 and numero <= 10:
                if numero == segredo:
                            print("-------------------------------------------")
                            print("         Voce acertou!!! parabens          ")
                            print("-------------------------------------------")
                else:
                            print("voce errou!! tente novamente")
                            tentativa -=1
            else:
                print("Valor Invalido")
                recomeco = str(input("Deseja continuar? [s/n]" ))
            
else:
    print("Fim de jogo") 
print("Fim de jogo")