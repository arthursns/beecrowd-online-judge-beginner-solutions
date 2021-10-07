valor = input()

valor = float(valor)

notas100 = valor // 100
valor = valor - (100 * notas100)

notas50 =  valor // 50
valor = valor - (50 * notas50)

notas20 = valor // 20
valor = valor - (20 * notas20)

notas10 = valor // 10
valor = valor - (10 * notas10)

notas5 = valor // 5
valor = valor - (5 * notas5)

notas2 = valor // 2
valor = valor - (2 * notas2)


moedas100 = valor // 1
valor = valor - (1 * moedas100)
moedas100=float('%.2f'% moedas100)
valor=float('%.2f'% valor)

moedas50 = valor // 0.5
valor = valor - (0.5 * moedas50)
moedas50=float('%.2f'% moedas50)
valor=float('%.2f'% valor)

moedas25 = valor // 0.25
valor = valor - (0.25 * moedas25)
m50=float('%.2f'%moedas25)
valor=float('%.2f'% valor)

moedas10 = valor // 0.10
valor = valor - (0.10 * moedas10)
moedas10=float('%.2f'% moedas10)
valor=float('%.2f'% valor)

moedas5 = valor // 0.05
valor = valor - (0.05 * moedas5)
moedas5=float('%.2f'% moedas5)
valor=float('%.2f'% valor)

moedas1 = valor * 100
moedas1=float('%.2f'% moedas1)
valor=float('%.2f'% valor)


print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(notas100)))
print("{} nota(s) de R$ 50.00".format(int(notas50)))
print("{} nota(s) de R$ 20.00".format(int(notas20)))
print("{} nota(s) de R$ 10.00".format(int(notas10)))
print("{} nota(s) de R$ 5.00".format(int(notas5)))
print("{} nota(s) de R$ 2.00".format(int(notas2)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(moedas100)))
print("{} moeda(s) de R$ 0.50".format(int(moedas50)))
print("{} moeda(s) de R$ 0.25".format(int(moedas25)))
print("{} moeda(s) de R$ 0.10".format(int(moedas10)))
print("{} moeda(s) de R$ 0.05".format(int(moedas5)))
print("{} moeda(s) de R$ 0.01".format(int(moedas1)))