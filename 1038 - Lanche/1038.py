input = input().split(" ")

a, b = input
a = int(a)
b = int(b)

if a == 1:
    valor = 4
elif a == 2:
    valor = 4.5
elif a == 3:
    valor = 5
elif a == 4:
    valor = 2
elif a == 5:
    valor = 1.5

total = float(b * valor)
total = format(total, ".2f")
print("Total: R$ " + str(total))