nomes = []
salarios = []

while True:
    nome = input("Digite o nome do funcionario (ou sair[para finalizar o programa.]) : ")
    if nome.lower == "sair":
        break
    salario = input("informe o salario do funcionario: ")

    nomes.append(nome)
    salarios.append(salario)

print(f"quantidade de alunos : {len(nomes)}")

print(f"Media do salario dos funcionarios : {sum(salarios)/len(nomes):.2f}")
print(f"Maior salario : {max(salarios)}")
print(f"Menor salario : {min(salarios)}")