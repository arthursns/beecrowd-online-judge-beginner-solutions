valor = float(input())

if 0<=valor<=400.00:
    valorNovo = valor * 1.15
    reajuste = valorNovo - valor
    porcentagem = 15

elif(400.01<=valor<=800.00):
    valorNovo = valor * 1.12
    reajuste = valorNovo - valor
    porcentagem = 12

elif(800.01<=valor<=1200):
    valorNovo = valor * 1.1
    reajuste = valorNovo - valor
    porcentagem = 10

elif(1200.01<=valor<=2000):
    valorNovo = valor * 1.07
    reajuste = valorNovo - valor
    porcentagem = 7

elif(valor>=2000):
    valorNovo = valor * 1.04
    reajuste = valorNovo - valor
    porcentagem = 4

valorNovo = format(valorNovo, ".2f")
reajuste = format(reajuste, ".2f")
print("Novo salario: " + str(valorNovo))
print("Reajuste ganho: " + str(reajuste))
print("Em percentual: " + str(porcentagem) + " %")