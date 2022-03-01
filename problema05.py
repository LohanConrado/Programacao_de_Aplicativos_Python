lista = [10,20,30,40,50,60,70]
posicao = 0

def numerar(posicao):
    x = len(lista)
    while (posicao < (x)):
        print("Posição ", (posicao + 1),":", lista[posicao])
        posicao = (posicao + 1)
    else:
        print("FIM")

print(numerar(posicao))