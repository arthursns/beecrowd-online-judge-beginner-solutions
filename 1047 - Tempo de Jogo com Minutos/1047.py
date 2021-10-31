x = input().split()

hi, mi, hf, mf = x

hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)

mit = (hi*60) + mi

mft = (hf*60) + mf

if(mit > mft):
    dHora = ((1440 - mit) + mft)//60
    dMin = ((1440 - mit) + mft) - (dHora * 60)

elif(mft > mit):
    dHora = (mft - mit)//60
    dMin = (mft - mit) - (dHora * 60)
else:
    dHora = 24
    dMin = 0

print("O JOGO DUROU " + str(dHora) + " HORA(S) E " + str(dMin) + " MINUTO(S)")