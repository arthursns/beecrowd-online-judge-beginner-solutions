x = input().split()
n1, n2, n3 = x
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)

if(n1 > n2 and n1 > n3):
    a = n1
    b = n2
    c = n3
elif(n2 > n1 and n2 > n3):
    a = n2
    b = n1
    c = n3
else:
    a = n3
    b = n1
    c = n2

if(a >= (b + c)):
    print("NAO FORMA TRIANGULO")
elif(a**2 == (b**2 + c**2)):
    print("TRIANGULO RETANGULO")
elif(a**2 > (b**2 + c**2)):
    print("TRIANGULO OBTUSANGULO")
elif(a**2 < (b**2 + c**2)):
    print("TRIANGULO ACUTANGULO")
if(a == b == c):
    print("TRIANGULO EQUILATERO")
elif(a == b or a == c or b == c):
    print("TRIANGULO ISOSCELES")