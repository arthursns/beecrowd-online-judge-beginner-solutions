valor = float(input())

if 0<=valor<=400.00:
    valorNovo = valor * 1,15
    reajuste = valorNovo - valor
    print("Novo salario: " + str(valorNovo))
    print("Reajuste ganho: " + str(reajuste))
    print("Em percentual: 15 %")
elif(400.01<=valor<=800.00):
    valorNovo = valor * 1,12
    reajuste = valorNovo - valor
    print("Novo salario: " + str(valorNovo))
    print("Reajuste ganho: " + str(reajuste))
    print("Em percentual: 12 %")
elif(800.01<=valor<=1200):
    valorNovo = valor * 1,1
    reajuste = valorNovo - valor
    print("Novo salario: " + str(valorNovo))
    print("Reajuste ganho: " + str(reajuste))
    print("Em percentual: 10 %")
elif(1200.01<=valor<=2000):
    valorNovo = valor * 1,7
    reajuste = valorNovo - valor
    print("Novo salario: " + str(valorNovo))
    print("Reajuste ganho: " + str(reajuste))
    print("Em percentual: 7 %")
elif(valor>=2000):
    valorNovo = valor * 1,4
    reajuste = valorNovo - valor
    print("Novo salario: " + str(valorNovo))
    print("Reajuste ganho: " + str(reajuste))
    print("Em percentual: 4 %")