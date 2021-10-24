x = input().split()
inicio , fim = x
inicio = int(inicio)
fim = int(fim)

if(inicio > fim):
    duracao = (24 - inicio) + fim
elif(fim > inicio):
    duracao = fim - inicio
else:
    duracao = 24

print("O JOGO DUROU " + str(duracao) + " HORA(S)")