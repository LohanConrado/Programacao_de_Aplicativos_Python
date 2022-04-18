valor_total = 0
valor_pago = 0
troco = 0
real = [200,100,50,20,10, 5,2,1,0.50,0.25,0.10,0.05, .01]
quantidade = 0
continuar_parar = "S"
separador = "=================================="
posicao = 0

while(continuar_parar != "N"):

    valor_total = float(input("Digite o valor total: R$ "))
    valor_pago = float(input("Digite o valor pago: R$ "))
    print(separador)
    troco = ((valor_total - valor_pago)* - 1)
    troco = round(troco,2) 
    
    if (troco == 0):
        print("Não há necessidade de troco")
    else:
        if (troco < 0):
            print("Está faltando dinheiro")
        
        #Calcula o troco a partir daqui
        elif (troco > 0):
            print("Troco:",troco,"\n")
            
            for cada in real:
                quantidade = 0
                while troco >= cada:
                    troco = round(troco - cada, 2)
                    quantidade += 1
                if cada > 1 and quantidade > 0:
                    print(f"Total {quantidade} notas de {cada}")
                elif quantidade > 0:
                    print(f"Total {quantidade} moedas de {cada}")
                              
      #Codigo antigo, complexo demais e não funciona          
    """ while True:
            if troco >= real[posicao]:
                troco -= real[posicao]
                quantidade += 1
            else: 
                # Imprimir cedulas
                if (posicao < 7):
                        print(f"Total {quantidade} notas de {real[posicao]}")
                        posicao += 1
                # Imprimir moedas
                elif (posicao > 6):
                    print(f"Total {quantidade} moedas de {real[posicao]}")
                    posicao += 1
                    
                quantidade = 0
                
            if troco == 0 or troco < 0.05:
                quantidade == 0
                posicao == 0
                break
        """
           
    continuar_parar = input("Deseja continuar? (S/N): ")
    print(separador)
