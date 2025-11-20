marca = ["Toyota", "Honda", "Ford"]
modelo = ["Corolla", "Civic", "Focus"]

Usuario = {
    "compras" : [marca, modelo],
    "Saldo_disponivel" : 0.0,
    "nome" : "",
    "telefone" : 0.0,
}

Venda = {
    "marca": marca,
    "modelo": modelo,
    "FIPE": [90000, 85000, 80000],
}

def desconto(preco):
    return preco - (preco * (12/100))




print("-----SEJA BEM-VINDO A CONCESSIONARIA-----")
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
saldo = float(input("Digite o saldo disponível: R$ "))

Usuario["nome"] = nome
Usuario["telefone"] = telefone  
Usuario["Saldo_disponivel"] = saldo

sair = True

while sair:

    print("\n-----MENU DE OPÇÕES-----")
    print("1 - Venda de veiculos")
    print("2 - Aluguel de veiculos")
    print("3 - Compra de veiculos")
    print("4 - Sair")


    opcao = int(input("Escolha uma opção (1-4): "))

    match opcao:
        case 1:
            print("Opção de Venda selecionada.")

            for i in range (len(Venda["marca"])):
               print(f"Marca: {Venda['marca'][i]}-{i+1} ")
            marca_escolhida = int(input("Escolha a marca do veiculo que deseja comprar (1-3): ")) -1

            for j in range (len(Venda["modelo"])):
               print(f"Modelo: {Venda['modelo'][j]}-{j+1} ")

            modelo_escolhido = int(input("Escolha o modelo do veiculo que deseja comprar (1-3): ")) -1
            preco = Venda["FIPE"][(marca_escolhida)]
            print(f"O preço do veiculo escolhido é R$ {preco:.2f}.\nCom um desconto de 12%, o valor final é R$ {desconto(preco):.2f}.")

            confirmacao = input("Deseja finalizar a compra? (s/n): ").strip().lower()
            if confirmacao == 's':
                if Usuario["Saldo_disponivel"] >= desconto(preco):
                    print("Compra realizada com sucesso!")
                    Usuario["Saldo_disponivel"] -= desconto(preco)
                    Usuario["compras"].append([Venda["marca"][marca_escolhida], Venda["modelo"][modelo_escolhido]])
                    print(f"Saldo restante: R$ {Usuario['Saldo_disponivel']:.2f}")
                else:
                    print("Saldo insuficiente para a compra.")
              
            else:
                print("Compra cancelada.")

        case 2:
            print("Opção de Aluguel selecionada.")
            print("Informe o veiculo para a locoação da lista seguinte.")
            for i in range(len(Venda["marca"])):
                for j in range (len(Venda["modelo"])):
                   print(f"marca: {Venda['marca'][i]}-{i+1} || modelo: {Venda['modelo'][j]} ")

            marca_alugada = int(input("Escolha a marca do veiculo que deseja alugar (1-3): ")) -1

        case 3:
            print("Opção de Compra selecionada.")

        case 4:
            print("Saindo...")
            sair = False

        case _:
            print("Opção inválida.")
