distancia = input()
combustivel = input()

distancia = int(distancia)
combustivel = float(combustivel)

consumo = distancia/combustivel

consumo = format(consumo, ".3f")

print(str(consumo) + " km/l")