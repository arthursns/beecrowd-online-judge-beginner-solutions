valor = input()

valor = int(valor)
print(str(valor))

notas100 = valor // 100
valor = valor - (100 * notas100)

notas50 =  valor// 50
valor = valor - (50 * notas50)

notas20 = valor // 20
valor = valor - (20 * notas20)

notas10 = valor //10
valor = valor - (10 * notas10)

notas5 = valor //5
valor = valor - (5 * notas5)

notas2 = valor //2
valor = valor - (2 * notas2)

notas1 = valor
valor = valor - (1 * notas1)

print(str(notas100) + " nota(s) de R$ 100,00")
print(str(notas50) + " nota(s) de R$ 50,00")
print(str(notas20) + " nota(s) de R$ 20,00")
print(str(notas10) + " nota(s) de R$ 10,00")
print(str(notas5) + " nota(s) de R$ 5,00")
print(str(notas2) + " nota(s) de R$ 2,00")
print(str(notas1) + " nota(s) de R$ 1,00")