D = input().split(" ")

A, B, C = D

A = int(A)
B = int(B)
C = int(C)

maiorAB = (A + B + abs(A - B))/2

maior = (maiorAB + C + abs(maiorAB - C))/2

maior = int(maior)

print(str(maior) + " eh o maior")