marca = []
modelo = []

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
    print("Veículos disponíveis para aluguel:")
    for i, v in enumerate(Venda["veiculos"]):
        print(f"{i+1} - {v['marca']} {v['modelo']} || {v['status']}")
        
    escolhido = int(input(f"Escolha o veículo (1-{i+1}): ")) - 1

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
            for indice_marca in range(len(geral["carros"])):
                if (geral["carros"][indice_marca]["marca"].lower() == marca_venda and
                    geral["carros"][indice_marca]["modelo"].lower() == modelo_venda):
                     existe = True
                     break
                       
            if  not existe:
                print("Veiculo não encontrado na lista .")
                continue

            preco = geral["carros"][indice_marca]["FIPE"]
            preco_descontado = desconto(preco, 12, False)

            print(f"O preço do veiculo escolhido é R$ {preco:.2f}.\nCom um desconto de 12%, o valor final é R$ {preco_descontado:.2f}.")

            confirmacao = input("Deseja finalizar a compra? (s/n): ").strip().lower()

            if confirmacao == 's':
                    print("Compra realizada com sucesso!")
                    Usuario["Saldo_disponivel"] += preco_descontado
                 
                    adicionar_veiculo(marca_venda.title(), modelo_venda.title(), preco)
                    print(f"Saldo total: R$ {Usuario['Saldo_disponivel']:.2f}")
            else:
                    print("venda cancelada.")
        case 2:
            confirmacao2 = 's'
            while confirmacao2 != 'n':
                print("Opção de Aluguel selecionada.")
                print("Informe o veiculo para a locoação da lista seguinte.")
                
                carro_alugado = lista_veiculos()
                print("escolheu o veiculo:", Venda["veiculos"][carro_alugado]["marca"], Venda["veiculos"][carro_alugado]["modelo"]) 
                  
                
                dias = int(input("Por quantos dias deseja alugar o veiculo? o aluguel custa R$77,00 por dia. "))
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
               
                confirmacao2=input("deseja alugar mais algum veiculo? (s/n): ").strip().lower()


        

        case 3:
            pass  # Adicione a lógica de compra de veículos aqui futuramente
            

        
