A = input().split(" ")
B = input().split(" ")

codigo1, numero1, valor1 = A
codigo2, numero2, valor2 = B

VALOR = (int(numero1)*float(valor1)) + (int(numero2)*float(valor2))

VALOR = format(VALOR, '.2f')

print('VALOR A PAGAR: R$ ' + str(VALOR))