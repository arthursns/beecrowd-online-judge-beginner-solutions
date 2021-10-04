data = input()

data = int(data)

anos = data // 365
data = data - (anos * 365)
print(str(anos) + " ano(s)")

meses = data // 30
data = data - (meses * 30)
print(str(meses) + " mes(es)")

dias = data
print(str(dias) + " dia(s)")
