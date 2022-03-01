#Codigo do primeiro problema

from pydoc import doc


L = [5, 7, 2, 9, 4, 1, 3]
i = 0
y = 0
maior = 0
menor = 0
tamanho = len(L)
#Tamanho da lista
print("Temos ",tamanho," numeros")

#--------------------------------------------------------------------------------#

#maior valor
while (i < 7):
    if maior < L[i]:
        maior = L[i]
        i+=1
    else:
        i+=1
print("O maior numero é ", maior)

#menor valor
while (y < 7):
    if menor < L[y]:
        menor = L[y]
        y+=1
    else:
        y+=1

print("O menor numero é ", menor)

#--------------------------------------------------------------------------------#

#Ordem Crescente
print("Lista em ordem crescente:","\n",sorted(L))

#--------------------------------------------------------------------------------#

#Ordem Decrescente
print("Lista em ordem decrescente:","\n",sorted(L,reverse=True))