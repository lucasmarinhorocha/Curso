
numeros = [50,10,5] 
print(numeros)
print(numeros[0])
numeros[2] = 20
print(numeros)

numeros.append(15) #adiciona um novo elemento no final da lista
print(numeros)

numeros.remove(10) #remove o elemento 10 da lista
print(numeros)

print(len(numeros)) #mostra o tamanho da lista

notas = sum(numeros) #soma todos os elementos da lista
media = notas/len(numeros)
print(f"media total: {media:.0f}") #mostra a média dos elementos da lista