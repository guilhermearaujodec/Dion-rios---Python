# Exercício 02 
 
# Preencha um dicionário com as informações de 5 produtos.  - Utilize o nome do produto como chave e o preço como valor.  - Solicite os dados ao usuário.  Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00 
# Exemplo:  Veja um exemplo da estrutura do dicionário.  {'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}

dic_produtos = {}
for n in range(5):
    produto = input('insira o nome do produto: ')
    if produto == '':
        break
    else:
        preco = float(input('Preço: '))
        dic_produtos[produto] = preco                    # insere no dicionário

print('---------------------------------')
print(dic_produtos)
print('---------------------------------')

for chave, valor in dic_produtos.items():
    
    if valor >= 50:
        print('---------------------------------')
        print(f'Nome: {chave} - Preço: {valor}')
        print('---------------------------------')