inse1 = int(input("Escolha um dos lanches abaixo: \n 100 - Cachorro Quente \n 101 - Bauru Simples "
                  "\n 102 - Bauru com ovo \n 103 - Hamburguer \n 104 - Cheeseburguer\n "
                  "105 - Suco \n 106 - Regrigerante \n Insira sua operação (101, 102, 103, 104, 105, 106): "))

num2 = int(input('Insira a quantidade de produtos: '))

if inse1 == 100:
    calc1 = num2 * 1.20
    print(f"O valor do lanche será {calc1:.2f}")
elif inse1 == 101:
    calc2 = num2 * 1.30
    print(f"O valor do lanche será {calc2:.2f}")
elif inse1 == 102:
    calc3 = num2 * 1.50
    print(f"O valor do lanche será {calc3:.2f}")
elif inse1 == 103:
    calc4 = num2 * 1.20
    print(f"O valor do lanche será {calc4:.2f}")
elif inse1 == 104:
    calc5 = num2 * 1.70
    print(f"O valor do lanche será {calc5:.2f}")
elif inse1 == 105:
    calc6 = num2 * 2.20
    print(f"O valor do lanche será {calc6:.2f}")
elif inse1 == 106:
    calc7 = num2 * 1.00
    print(f"O valor do lanche será {calc7:.2f}")
else:
    print("Insira um numero valido!")



