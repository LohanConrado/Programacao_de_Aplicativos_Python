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

# Metodo mais facil usando função do proprio Python: https://github.com/LohanConrado/Programacao_de_Aplicativos/blob/c31e3b879ed98fa57ab47bc86cb4394f0d2d7949/problema05_enumarate.py
