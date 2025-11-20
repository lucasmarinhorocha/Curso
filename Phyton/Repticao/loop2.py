
while True :
    nome = input("usuario: ").strip().lower()
    senha = input("senha: ").lower()
    if len(senha) > 4:
        print("A senha deve ter no maximo 4 caracteres")
        
        if nome == "admin" and senha == "1234":

            print("Acesso permitido")
            break
        else:
            print("Acesso negado, tente novamente")