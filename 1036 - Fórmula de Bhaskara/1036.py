dados = input().split()

a, b, c = dados

a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - 4 * a * c

if a == 0.0  or delta < 0:
    print('Impossivel calcular')
else:
    r1 = (- b + ((delta) ** (1/2))) / (2*a)
    r1 = format(r1 , ".5f")
    r2 = (- b - ((delta) ** (1/2))) / (2*a)
    r2 = format(r2 , ".5f")
    print("R1 = " + str(r1))
    print("R2 = " + str(r2))