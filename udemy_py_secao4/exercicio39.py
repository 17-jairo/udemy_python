valor_premio = 780000
first_winner = 0.46 * valor_premio
second_winner = 0.32 * valor_premio
third_winner = (1-0.46-0.32) * valor_premio

print(f"O valor obtido pelo primeiro colocado é R$ {first_winner},\n Já o valor para o segundo colocado é R$ {second_winner}. \nPara o terceiro colocado o valor será: R$ {third_winner:.1f}")