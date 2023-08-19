print("Abaixo estão disponíveis as seguintes operações: \n 1 - Soma de dois números. "
      "\n 2 - Diferença entre 2 números (maior pelo menor). "
      "\n 3 - Produto entre 2 números. "
      "\n 4 - Divisão entre dois números (o denominador não pode ser zero.")

num1 = int(input("Digite o número referente a opção escolhida: "))

if num1 == 1:
      som1 = int(input("Digite o primeiro valor: "))
      som2 = int(input("Digite o segundo valor: "))
      calc1 = som1 + som2
      print(f"A soma dos dois numeros é {calc1}!")
elif num1 == 2:
      dre1 = int(input("Digite o primeiro valor: "))
      dre2 = int(input("Digite o segundo valor: "))
      calc2 = abs(dre1 - dre2)
      print(f"A diferença entre dois numeros é {calc2}!")
elif num1 == 3:
      pro1 = int(input("Digite o primeiro valor: "))
      pro2 = int(input("Digite o segundo valor: "))
      calc3 = pro1 * pro2
      print(f"O produto dos dois numeros é {calc3}!")
elif num1 == 4:
      div1 = int(input("Digite o numerador: "))
      div2 = int(input("Digite o denominador: "))
      if div2 > 0:
            calc4 = div1 / div2
            print(f"A divisão dos dois numeros é {calc4}!")
      else:
            print("Insira um denominador maior que zero! ")
else:
      print ("Número invalido, insira o numero correspondente a operação desejada!")

