horas = int(input("Insira o numero de horas: "))
minutos = int(input("Insira o numero de minutos: "))
segundos = int(input("Insira o numero de segundos: "))
duracao = int(input("Insira o numero de duração: "))

# conversoes da duracao de segundos para horas/minutos

h_segundos = horas * 3600 + minutos * 60 + segundos
s_segundos = h_segundos + duracao

conv1 = s_segundos // 3600
conv2 = s_segundos % 3600 // 60
conv3 = s_segundos % 60

# imprimindo a solucão

print(f"O horário de término será {conv1} horas, {conv2} minutos e {conv3} segundos.")


