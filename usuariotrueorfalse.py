valorpedido=int(input('valor pedido'))

valorentrega=0

usuariofidelidade=input('usuario')



if(usuariofidelidade =="sim"):

    fidelidade = True

else:

    fidelidade=False

    

if(valorpedido<10):

    valorentrega=5

elif(valorpedido >= 10 and valorpedido <20):

    valorentrega = 3

else:

    valorentrega=0 



if(fidelidade == True and valorentrega >= 2):

    valorentrega = valorentega - 2 



print(f"o valor da entrega é: {valorentrega}")