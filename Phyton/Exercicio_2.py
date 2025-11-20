compra = int(input("informe o valor da compra: "))

if( compra < 100):
    print("Sem desconto, valor inteiro de: ", compra)
else :
    print("desconto aplicado de: ", compra *0.9)