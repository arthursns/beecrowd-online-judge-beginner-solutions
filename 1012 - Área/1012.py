D = input().split(" ")

A, B, C = D

A = float(A)
B = float(B)
C = float(C)

areaTriangulo = (A*C)/2
areaCirculo = (3.14159)*(C**2)
areaTrapezio = ((A+B)*C)/2
areaQuadrado = B*B
areaRetangulo = A*B

areaTriangulo = format(areaTriangulo, ".3f")
areaCirculo = format(areaCirculo, ".3f")
areaTrapezio = format(areaTrapezio, ".3f")
areaQuadrado = format(areaQuadrado, ".3f")
areaRetangulo = format(areaRetangulo, ".3f")

print("TRIANGULO: " + str(areaTriangulo))
print("CIRCULO: " + str(areaCirculo))
print("TRAPEZIO: " + str(areaTrapezio))
print("QUADRADO: " + str(areaQuadrado))
print("RETANGULO: " + str(areaRetangulo))