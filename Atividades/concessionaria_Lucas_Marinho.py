
Usuario = {
    "compras" : [],
    "Saldo_disponivel" : 0.0,
    "nome" : "",
    "telefone" : 0.0,
}
geral= {
     "carros": [
    {"marca": "Toyota",     "modelo": "Corolla",     "FIPE": 90000, "status": "DISPONIVEL"},
    {"marca": "Honda",      "modelo": "Civic",       "FIPE": 85000, "status": "DISPONIVEL"},
    {"marca": "Ford",       "modelo": "Focus",       "FIPE": 80000, "status": "DISPONIVEL"},
    {"marca": "Chevrolet",  "modelo": "Onix",        "FIPE": 70000, "status": "DISPONIVEL"},
    {"marca": "Volkswagen", "modelo": "Gol",         "FIPE": 65000, "status": "DISPONIVEL"},
    {"marca": "Fiat",       "modelo": "Argo",        "FIPE": 62000, "status": "DISPONIVEL"},
    {"marca": "Hyundai",    "modelo": "HB20",        "FIPE": 68000, "status": "DISPONIVEL"},
    {"marca": "Renault",    "modelo": "Kwid",        "FIPE": 55000, "status": "DISPONIVEL"},
    {"marca": "Nissan",     "modelo": "Versa",       "FIPE": 78000, "status": "DISPONIVEL"},
    {"marca": "Jeep",       "modelo": "Renegade",    "FIPE": 120000, "status": "DISPONIVEL"}
]

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
    print("Veículos disponíveis:")
    for i, v in enumerate(Venda["veiculos"]):
        print(f"{i+1} - {v['marca']} {v['modelo']} || {v['status']}")
        
    escolhido = int(input(f"Escolha o veículo (1-{i+1}): ")) - 1
    if escolhido < 0 or escolhido >= len(Venda["veiculos"]):
        print("Escolha inválida. Retornando ao menu principal.")
        return -1
    return escolhido

def adicionar_veiculo(marca, modelo, fipe):
    Venda["veiculos"].append({"marca": marca, "modelo": modelo, "FIPE": fipe, "status": "DISPONIVEL"})


def remover_veiculo(indice):
    if 0 <= indice < len(Venda["veiculos"]):
        del Venda["veiculos"][indice]
    else:
        print("Índice inválido. Nenhum veículo removido.")

def adicionar_Usuario_compra(i):
    Usuario["compras"].append({"marca": Venda["veiculos"][i]["marca"], "modelo": Venda["veiculos"][i]["modelo"], "FIPE": Venda["veiculos"][i]["FIPE"], "status": "DISPONIVEL"})
     
def menu():
    print("\n-----MENU DE OPÇÕES-----")
    print("1 - Venda de veiculos")
    print("2 - Aluguel de veiculos")
    print("3 - Compra de veiculos")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção (1-4) ou (0) em qualquer momento para voltar ao menu: "))
    return opcao


def retornar_ao_menu(voltar):
    if voltar <= 0 :
        return 

    print("-----SEJA BEM-VINDO A CONCESSIONARIA-----")
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
saldo = float(input("Digite o saldo disponível: R$ "))

Usuario["nome"] = nome
Usuario["telefone"] = telefone  
Usuario["Saldo_disponivel"] = saldo

sair = True

while sair:

    opcao = menu()

    match opcao:
        case 1:
            print("Opção de Venda selecionada.")
            print("Informe a marca e o modelo do veículo que deseja vender")

            marca_venda = input("Marca: ").title().strip()
            modelo_venda = input("Modelo: ").title().strip()

            if marca_venda == '0' or modelo_venda == '0':
                retornar_ao_menu(0)
                continue

            indice_marca = -1
            for i in range(len(geral["carros"])):
                if (geral["carros"][i]["marca"].lower() == marca_venda and
                    geral["carros"][i]["modelo"].lower() == modelo_venda):
                    indice_marca = i
                    break

            if indice_marca == -1:
                print("Veículo não encontrado na lista.")
                continue   

            preco = geral["carros"][indice_marca]["FIPE"]
            preco_descontado = desconto(preco, 12, False)

            print(f"O preço do veículo escolhido é R$ {preco:.2f}.")
            print(f"Com desconto de 12%, o valor final é R$ {preco_descontado:.2f}.")

            confirmacao = input("Deseja finalizar a venda? (s/n): ").strip().lower()

            if confirmacao == '0':
                retornar_ao_menu(0)
                continue

            if confirmacao == 's':
                print("Venda realizada com sucesso!")
                Usuario["Saldo_disponivel"] += preco_descontado

                adicionar_veiculo(marca_venda.title(), modelo_venda.title(), preco)

                print(f"Saldo total: R$ {Usuario['Saldo_disponivel']:.2f}")
            else:
                print("Venda cancelada.")

        case 2:
            confirmacao2 = 's'
            while confirmacao2 != 'n':
                print("Opção de Aluguel selecionada.")
                print("Informe o veiculo para a locoação da lista seguinte.")
                
                carro_alugado = lista_veiculos()

                if carro_alugado < 0 :
                    retornar_ao_menu(carro_alugado)  
                    break
                print("escolheu o veiculo:", Venda["veiculos"][carro_alugado]["marca"], Venda["veiculos"][carro_alugado]["modelo"]) 
                  
                dias = int(input("Por quantos dias deseja alugar o veiculo? o aluguel custa R$77,00 por dia. "))
                if dias == 0:
                    retornar_ao_menu(dias)  
                    break
                valor_aluguel = 77 * dias

                if(Usuario["Saldo_disponivel"] >= valor_aluguel):
                    print(f"Aluguel realizado com sucesso! Valor total: R$ {valor_aluguel:.2f}")
                    Usuario["Saldo_disponivel"] -= valor_aluguel
                    print(f"Saldo restante: R$ {Usuario['Saldo_disponivel']:.2f}")

                    adicionar_Usuario_compra(carro_alugado)
                    remover_veiculo(carro_alugado)
                    print(f"Veículo alugado adicionado ao seu histórico de compras.{Usuario['compras']}")
                else:
                    print("Saldo insuficiente para o aluguel.")
               
                confirmacao2 = input("deseja alugar mais algum veiculo? (s/n): ").strip().lower()

        case 3:
            loop = 's'
            while loop != 'n':
                print("Opção de Compra selecionada.")
                print("Informe o veiculo para a compra da lista seguinte.")
                carro_comprado = lista_veiculos()
                
                if carro_comprado < 0 :
                    retornar_ao_menu(carro_comprado)  
                    break

                preco_compra = Venda["veiculos"][carro_comprado]["FIPE"]
                preco_com_desconto = desconto(preco_compra, 25, True)

                print(f"O preço do veiculo escolhido é R$ {preco_compra:.2f}.\nCom um acrescimo de 25%, o valor final é R$ {preco_com_desconto:.2f}.")
                confirmacao3 = input("Deseja finalizar a compra? (s/n): ").strip().lower()
                if confirmacao3 == 's':
                    if(Usuario["Saldo_disponivel"] >= preco_com_desconto):
                        print("Compra realizada com sucesso!")
                        Usuario["Saldo_disponivel"] -= preco_com_desconto
                        print(f"Saldo restante: R$ {Usuario['Saldo_disponivel']:.2f}")

                        adicionar_Usuario_compra(carro_comprado)
                        remover_veiculo(carro_comprado)
                        print(f"Veículo comprado adicionado ao seu histórico de compras.{Usuario['compras']}")
                    else:
                        print("Saldo insuficiente para a compra.")

                loop = input("deseja comprar mais algum veiculo?(s/n): ").strip().lower()

        case 4:
            print("Saindo do sistema. Obrigado por visitar nossa concessionária!")
            sair = False

        case _:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
            

        
