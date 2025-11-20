print("----BEM VINDO----")
valor = float(input("digite o valor da compra"))
forma_pagamento = (input("forma de pagamento(debito/credito/dinheiro/pix)"))

if forma_pagamento == "dinheiro":
    total = valor *0.9
    print(f"Pagamento em dinheiro: {total}")
elif forma_pagamento == "pix":
    if valor >= 1000 :
        total = valor*0.85
        print(f"Pagamento em pix: {total}")
    elif valor >= 500 :
        total = valor*0.95
        print(f"Pagamento em pix: {total}")
elif forma_pagamento == "debito":
    total = valor
    print(f"pagamento em debito: {total}")
elif forma_pagamento == "credito":
    parcelas = int(input("parcelar em quanto"))
    if parcelas == 3:
        total = valor
        print(f"pagamento em credito separado em {parcelas}: sem juros {total/parcelas}, no total de {total}")
    elif parcelas == 4 :
         total = valor*1.10
         print(f"pagamento em credito separado em {parcelas}: com 10% de juros {total/parcelas}, no total de {total}")
    elif parcelas == 6 :
         total = valor*1.20
         print(f"pagamento em credito separado em {parcelas}: com 20% de juros {total/parcelas}, no total de {total}")
else:
    print("tente novamente")