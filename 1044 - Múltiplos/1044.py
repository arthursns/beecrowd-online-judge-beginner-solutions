x = input().split()

a, b = x
a = float(a)
b = float(b)

if(a >= b):
    maior = a
    menor = b
else:
    maior = b
    menor = a

if(maior%menor == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")