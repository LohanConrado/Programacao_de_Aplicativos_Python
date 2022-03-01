valores = [0,0,0,0]
i = 0
soma = 0
media = 0
print("Digite 4 valores!")

while (i < 4):
    valores[i] = (int(input("Valor ")))
    i+=1

soma = sum(valores[0:4])
media = soma / i

if media > 0:
    print("Sua média é: POSITIVA ","\n", media )
else:
    print("Sua média é: NEGATIVA ","\n", media )