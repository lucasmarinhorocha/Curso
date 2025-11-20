
nomes=()
while True:
  nome = input("Digite o nome do seu colega : ")
 
  if nome.lower() == "sair":
   break
nomes += (nome,)
   
   
print(f"o primeiro numero é: {nomes[0]}")
print(f"o ultimo numero é: {nomes[-1]}")
print(f"A quantidade de nomes é : {len(nomes)}")