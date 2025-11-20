numeros = ()
num_cinco = 0
while True:
    numero = int(input("Digite o número : "))
    
    if numero == -1:
        break
    if numero == 5:
        print("PO NUMERO 5 PASSOU AQUI !")
        numero += 1
        numeros +=(numero,)

print(f"os número digitados voram : {numeros}")
print(f"O número cinco apareceu : {num_cinco}")
print(f"O maior número digitado foi : {max(numeros)}")
print(f"O menor número digitado foi : {min(numeros)}")