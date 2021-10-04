tempo = input()

tempo = int(tempo)

horas = tempo // 60 ** 2
tempo = tempo - (horas * 60 ** 2)

minutos = tempo // 60
tempo = tempo - (minutos * 60)

segundos = tempo 

print(str(horas) + ":" + str(minutos) + ":" + str(segundos))
