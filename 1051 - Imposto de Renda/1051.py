salario = float(input())
imposto = 0
if 0<=salario<=2000.00:
    print("Isento")
elif 2000.01<=salario<=3000.00:
    imposto = (salario - 2000)/100*8
    imposto = format(imposto, ".2f")
    print("R$ " + str(imposto))
elif 3000.01<=salario<=4500.00:
    imposto = (salario - 3000)/100*18 + 80
    imposto = format(imposto, ".2f")
    print("R$ " + str(imposto))
elif 4500.00<salario:
    imposto = (salario - 4500)/100*28 + 80 + 270
    imposto = format(imposto, ".2f")
    print("R$ " + str(imposto))