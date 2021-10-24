x = input().split()

n1, n2, n3, n4 = x

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2) + (n2*3) + (n3*4) + n4)/10
print("Media: " + str(format(media, ".1f")))

if(media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
elif(media >= 5.0 and media < 6.9):
    print("Aluno em exame.")
    nExame = input()
    nExame = float(nExame)
    print("Nota do exame: " + str(format(nExame, ".1f")))
    nMedia = (media + nExame)/2
    if(nMedia > 5.0):
        print("Aluno aprovado.")
    elif(nMedia < 4.9):
        print("Aluno reprovado.")
    print("Media final: " + str(format(nMedia, ".1f")))