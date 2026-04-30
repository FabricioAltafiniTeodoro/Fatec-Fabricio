n = [0]

i = 1
while i != 0:
    num = int(input("digite numero: "))
  

    if num != 0:
        print("Lista Atualizada")
        n.append(num)
        n.sort()
        for num in n:
            print(num)
    else:
        print("programa encerrado!")
        break
                


    


