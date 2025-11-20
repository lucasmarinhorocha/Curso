print("*****SISTEMA BANCARIO*****")
nome =input("nome do cliente")
renda = float(input("Informe a sua renda mensal"))
valor_solicitado = float(input("Informe o valor do emprestimo desejado"))

parcelas = int(input("Quantas vezes voce ira parcelar o valor"))
historico = input("Possui o nome negativado? (SIM/NÃO):" )

valor_parcelas = valor_solicitado/parcelas

print(f"\nCliente: {nome}")
print(f"Valor do emprestimo{valor_solicitado:.2f}")
print(f"Parcelas: {parcelas:} x de reais: {valor_parcelas}")

if historico == "sim": 
    print("EMPRESTIMO NEGADO")
else :

    if valor_solicitado> renda*0.3:
       print("EMPRESTIMO NEGADO: PARCELAS EXEDEM 30% DA PARCELA")
    elif renda >= 5000 and valor_solicitado <=10000: 
       print("EMPRESTIMO APROVADO !!! valor total reduzido")
    elif renda >= 3000 and valor_solicitado < 5000: 
       print("EMPRESTIMO APROVADO !!! valor total padrão")
    else:
       print("EMPRESTIMO APROVADO !!! valor de risco")

print("\n==== ANALISE CONCLUIDA ====")