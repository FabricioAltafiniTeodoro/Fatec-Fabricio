print("Seja bem vindo(a) ao Mybank")
print("SIMULADOR DE EMPRESTIMO")

rep = "s"

while rep == "s":

    if rep == "s": 
        cliente = str(input("Voce ja é nosso clienet? s/n: " ))

        if cliente == "n":
            score = int(input("Digite o seu Score: "))
            vaempre = float(input("Valor desejado para o emprestimo: "))
            qtdpar = int(input("Quantidade de parcelas: "))
            segudese = str(input("Deseja incluir um segugo desemprego no seu emprestimo: s/n "))

            tacadas = 35

            if segudese == "s":
                taxa = 50
            else: 
                taxa = 0 
            
            iof = vaempre * 0.0038

            if score >= 0 and score <= 299:
                vatotal =  taxa + iof + tacadas + (vaempre + (vaempre * 0.20))
                vapar = vatotal / qtdpar
                vataxa = 20

            elif score >= 300 and score <= 499:
                vatotal =  taxa + iof + tacadas (vaempre + (vaempre * 0.15))
                vapar = vatotal / qtdpar
                vataxa = 15

            elif score >= 500 and score <= 699:
                vatotal =  taxa + iof + tacadas + (vaempre + (vaempre * 0.10))
                vapar = vatotal / qtdpar 
                vataxa = 10   

            elif score >= 700 and score <= 1000:
                vatotal =  taxa + iof + tacadas +(vaempre + (vaempre * 0.05))
                vapar = vatotal / qtdpar
                vataxa = 5

            print(" ")
            print("------Resultado--------")  
            print(" ")

            print("Quantidade de parcelas: ", qtdpar)
            print("Valor de parcelas: ", vapar)
            print("Taxa de juros: ", vataxa)
            print("Custo Efetivo total: ", vatotal)

            rep = str(input("Voce Quer continuar a simular: "))
            
        else:
            vaempre = float(input("Valor desejado para o emprestimo: "))
            qtdpar = int(input("Quantidade de parcelas: "))
            segudese = str(input("Deseja incluir um segugo desemprego no seu emprestimo: s/n "))

            vataxa = 0.3
            iof = vaempre * 0.038

            if segudese == "s":
                taxa = 50
            else: 
                taxa = 0 
                
            vatotal =  taxa + iof + tacadas + (vaempre + (vaempre * 0.03))
            vapar = vatotal / qtdpar 

            print(" ")
            print("------Resultado--------")  
            print(" ")

            print("Quantidade de parcelas: ", qtdpar)
            print("Valor de parcelas: ", vapar)
            print("Taxa de juros: ", vataxa)
            print("Custo Efetivo total: ", vatotal)

rep = str(input("Voce Quer continuar a simular: "))

          
    

