bet1 = int(input("First player, how much you are going to invest R$: "))
bet2 = int(input("Second player, how much you are going to invest R$: "))
bet3 = int(input("Third player, how much you are going to invest R$: "))
premio = int(input("The winner prize is R$: "))

# soma dos valores
calc1 = bet1 + bet2 + bet3

# calculando proporção
prop1 = (100 * bet1 / calc1) / 100
prop2 = (100 * bet2 / calc1) / 100
prop3 = (100 * bet3 / calc1) / 100

# Imprimindo o resultado

print(f"The prize for the first player will be R$ {prop1 * premio:.2f},\n For the player two will be R$ {prop2 * premio:.2f},\n And for the third will be R$ {prop3 * premio:.2f}.  ")
