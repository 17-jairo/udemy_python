# Inicializar variáveis para a soma das notas e a contagem de notas
soma_notas = 0
contador_notas = 0

# Solicitar ao aluno que insira notas até que uma nota inválida seja inserida
while True:
    nota = float(input("Digite uma nota (entre 10 e 20, ou valor inválido para encerrar): "))

    # Verificar se a nota é válida (entre 10 e 20)
    if 10 <= nota <= 20:
        soma_notas += nota
        contador_notas += 1
    else:
        # Se a nota não for válida, sair do loop
        break

# Verificar se pelo menos uma nota válida foi inserida
if contador_notas > 0:
    # Calcular a média aritmética
    media = soma_notas / contador_notas
    print(f"A média das notas inseridas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")

