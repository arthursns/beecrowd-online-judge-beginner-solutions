tempo = input()
velocidade = input()

tempo = int(tempo)
velocidade = int(velocidade)

distancia = tempo * velocidade

litros = distancia / 12

litros = format(litros, ".3f")

print(litros)