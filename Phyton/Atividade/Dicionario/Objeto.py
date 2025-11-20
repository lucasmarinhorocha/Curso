

carro = {
    "marca": "Toyota", 
    "modelo": "Corolla",
    "ano": 2020,
    "cores": ["vermelho", "preto", "branco"],
}
# Acessar a lista dentro do dicionário 
print(carro["cores"][2]) 

#atualizar o valor de uma chave
carro["ano"].add(1)  # Incrementa o ano em 1

carro["KM"] = 45000

# mostrar as chaves e valores do dicionário
for chave, valor in carro.items():
    print(f"{chave} : {valor}")
