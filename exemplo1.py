# DICIONÁRIO

# dicionário vazio
dicionario = {}

# dicionário com itens
dicionario = {'name': 'Paulo', 'age': 30, 'job': 'Dev'}
print(dicionario)

# acessar um item
print(dicionario['age'])

# alterar um valor
dicionario['age'] = 31
print(dicionario)

# inserir nova chave e novo valor
dicionario['email'] = 'aaa@gmail.com'
print(dicionario)

# remover um item
dicionario.pop('job')
print(dicionario)

# preencher um dicionário para cadastro de alunos
alunos = {}
while True:
    rm = input('RM: ')
    if rm == '':
        break
    if rm not in alunos:
        nome = input('Nome: ')
        alunos[rm] = nome                    # insere no dicionário
    else:
        print('O RM já está cadastrado')
print(alunos)

# Declarando o Dicionário

dicionario = {
    'name': 'Paulo'
    'age': '30'
    'job': 'dev'
}

# percorrer as chaves
for chave in dicionario.keys():
    print(chave)

# percorrer os valores
for valor in dicionario.values():
    print(valor)
# percorrer os valores
for chave, valor in dicionario.items():
    print(f'RM: {chave} - Nome: {valor}')

# dicionario armazenando listas
notas = {'rm1234': [7, 8, 9.0], 'rm4567': [6, 8.5, 10], 'rm2222': [5, 9, 10]}
print(notas['rm1234'] [2])
notas['rm1234'] [0] = 7.75
print(notas)

# dicionario de dicionarios
alunos = {'rm1234': {'nome': 'Ana', 'turma': '1ESPG', 'notas': [8, 9, 10]},
          'rm8766': {'nome': 'Pedro', 'turma': '1ESPG', 'notas': [6, 9, 8]}}

print(alunos['rm8766']['turma'])
print(alunos['rm8766']['notas'])