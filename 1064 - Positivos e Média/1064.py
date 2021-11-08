a = float(input())
contagem = 0
media = 0

if a > 0:
    contagem = contagem + 1
    media = media + a

b = float(input())
if b > 0:
    contagem = contagem + 1
    media = media + b

c = float(input())
if c > 0:
    contagem = contagem + 1
    media = media + c

d = float(input())
if d > 0:
    contagem = contagem + 1
    media = media + d

e = float(input())
if e > 0:
    contagem = contagem + 1
    media = media + e

f = float(input())
if f > 0:
    contagem = contagem + 1
    media = media + f

print(str(contagem) + " valores positivos")

media = media/contagem
media = format(media, ".1f")

print(media)