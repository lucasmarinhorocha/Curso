marca = ["Toyota", "Honda", "Ford"]
modelo = ["Corolla", "Civic", "Focus"]

Usuario = {
    "compras" : [marca, modelo],
    "Saldo_disponivel" : 0.0,
    "nome" : "",
    "telefone" : 0.0,
}

Venda = {
    "veiculos": [
        {"marca": "Toyota", "modelo": "Corolla", "FIPE": 90000, "status": "DISPONIVEL"},
        {"marca": "Honda",  "modelo": "Civic",   "FIPE": 85000, "status": "DISPONIVEL"},
        {"marca": "Ford",   "modelo": "Focus",   "FIPE": 80000, "status": "DISPONIVEL"}
    ]
}


def desconto(preco):
    return preco - (preco * (12/100))

def lista_veiculos():
    print("Veículos disponíveis para aluguel:")
    for i, v in enumerate(Venda["veiculos"]):
        print(f"{i+1} - {v['marca']} {v['modelo']} || {v['status']}")
    escolhido = int(input("Escolha o veículo (1-3): ")) - 1
    return escolhido




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

            

            marca_escolhida = lista_veiculos()
            preco = Venda["veiculos"][marca_escolhida]["FIPE"]

            print(f"O preço do veiculo escolhido é R$ {preco:.2f}.\nCom um desconto de 12%, o valor final é R$ {desconto(preco):.2f}.")

            confirmacao = input("Deseja finalizar a compra? (s/n): ").strip().lower()
            if confirmacao == 's':
                if Usuario["Saldo_disponivel"] >= desconto(preco):
                    print("Compra realizada com sucesso!")
                    Usuario["Saldo_disponivel"] -= desconto(preco)
                    Usuario["compras"].append([Venda["marca"][marca_escolhida], Venda["modelo"][marca_escolhida]])
                    print(f"Saldo restante: R$ {Usuario['Saldo_disponivel']:.2f}")
                else:
                    print("Saldo insuficiente para a compra.")
              
            else:
                print("Compra cancelada.")

        case 2:
            confirmacao2 = 's'
            while confirmacao2 != 'n':
                print("Opção de Aluguel selecionada.")
                print("Informe o veiculo para a locoação da lista seguinte.")
                
                carro_alugado = lista_veiculos()
                print("\n ") 

                

                if (Venda["veiculos"][carro_alugado]["status"] == "INDISPONIVEL"):
                    print("Veiculo indisponivel para aluguel.")
                    break
            dias = int(input("Por quantos dias deseja alugar o veiculo? o aluguel custa R$77,00 por dia. "))
            valor_aluguel = 77 * dias

            if(Usuario["Saldo_disponivel"] >= valor_aluguel):
                    print(f"Aluguel realizado com sucesso! Valor total: R$ {valor_aluguel:.2f}")
                    Usuario["Saldo_disponivel"] -= valor_aluguel
                    print(f"Saldo restante: R$ {Usuario['Saldo_disponivel']:.2f}")
                    Venda["veiculos"][carro_alugado]["status"] = "INDISPONIVEL"

            else:
                    print("Saldo insuficiente para o aluguel.")
                
            confirmacao2=input("deseja alugar mais algum veiculo? (s/n): ").strip().lower()


        

        case 3:
            print("Opção de Compra selecionada.")

        case 4:
            print("Saindo...")
            sair = False

        case _:
            print("Opção inválida.")
