num1 = int(input("Insira o tempo em segundos: "))
horas = num1/3600
minutos = num1/60

print(f"O horario é {horas:.0f} em horas {minutos:.0f} em minutos e {num1:.0f} em segundos")

'''
num1 = int(input("Insira o tempo em segundos: "))
horas = num1 // 3600  # Usamos divisão inteira para obter as horas completas
minutos = (num1 % 3600) // 60  # Calculamos os minutos restantes após remover as horas
segundos = num1 % 60  # Calculamos os segundos restantes

print(f"O horário é {horas} horas, {minutos} minutos e {segundos} segundos.")

'''