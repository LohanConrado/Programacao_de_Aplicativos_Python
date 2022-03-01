valores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0
x = 0
y = 0
maior = 0
menor = 30
soma = 0
media = 0
print("Digite 20 valores!")

while (i < 20):
    valores[i] = (int(input("Valor ")))
    i+=1

while (x < 20):
    if maior < valores[x]:
        maior = valores[x]
        x+=1
    else:
        x+=1

while (y < 20):
    if menor > valores[y]:
        menor = valores[y]
        y+=1
    else:
        y+=1

soma = sum(valores[0:20])
media = soma / i

print("Média: ","\n",media,"\n","--------------------","\n","Maior numero: ", "\n",maior,"\n","--------------------","\n"," Menor numero: ","\n",menor,"\n","--------------------")