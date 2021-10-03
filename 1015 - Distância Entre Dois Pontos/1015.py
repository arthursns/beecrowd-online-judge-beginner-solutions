import math

P1 = input().split(" ")
P2 = input().split(" ")

XP1, YP1 = P1
XP2, YP2 = P2

XP1 = float(XP1)
YP1 = float(YP1)
XP2 = float(XP2)
YP2 = float(YP2)

distancia = math.sqrt(((XP2 - XP1)**2) + ((YP2 - YP1)**2))

distancia = format(distancia, ".4f")

print(str(distancia))