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


def desconto(preco, percentual,acresimo):
    if acresimo == True:
         return preco + (preco * (percentual/100))
    else:
         return preco - (preco * (percentual/100))

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
            print("informe a marca e o modelo do veiculo que deseja vender")
            marca_venda = input("Marca: ").lower().strip()
            modelo_venda = input("Modelo: ").lower().strip()
            
            existe = False
            for indice_marca in range(len(Venda["veiculos"])):
                if (Venda["veiculos"][indice_marca]["marca"].lower() == marca_venda and
                    Venda["veiculos"][indice_marca]["modelo"].lower() == modelo_venda):
                     existe = True
                     break
                       
            if not existe:
                print("Veiculo não encontrado na lista de vendas.")
                continue

            preco = Venda["veiculos"][indice_marca]["FIPE"]
            preco_descontado = desconto(preco, 12, False)

            print(f"O preço do veiculo escolhido é R$ {preco:.2f}.\nCom um desconto de 12%, o valor final é R$ {preco_descontado:.2f}.")

            confirmacao = input("Deseja finalizar a compra? (s/n): ").strip().lower()
            if confirmacao == 's':
                    print("Compra realizada com sucesso!")
                    Usuario["Saldo_disponivel"] += preco_descontado
                    Venda["veiculos"].append({"marca": marca_venda, "modelo": modelo_venda, "FIPE": preco, "status": "DISPONIVEL"})
                    print(f"Saldo total: R$ {Usuario['Saldo_disponivel']:.2f}")
            else:
                    print("venda cancelada.")
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
