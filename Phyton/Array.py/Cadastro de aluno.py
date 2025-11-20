nota = []
aluno = []

print("----- Cadastro de Alunos -----")

while True:
    opcao = int(input("oque voce deseja?\n 1-cadastrar aluno\n 2-colocar notas\n 3-mostrar media\n 4-remover nota\n 5-sair\n"))

    match opcao:

        case 1:      
            alunos = input("Digite nome do aluno : ")
            aluno.append(alunos)
           
        case 2:
            notas_aluno = float(input("Digite a nota do aluno: "))
            nota.append(notas_aluno)
           
        case 3:
            media = sum(nota) / len(nota)
            print(f"A media da turma é: {media:.2f}")
            
        case 4:
            print("Notas atuais:", nota)
            remover_nota = float(input("Digite a nota que deseja remover: "))
            if remover_nota in nota:
                nota.remove(remover_nota)
                print("Nota removida com sucesso.")
            else:
                print("Nota não encontrada.")
          
        case 5:
            print("Saindo do programa.")
            break
