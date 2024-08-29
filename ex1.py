# Exercício 01 
# Preencha um dicionário com as informações de 5 pessoas.  - Utilize o cpf da passoa como chave e o nome como valor.  - Solicite os dados ao usuário. 
# Exemplo:  Veja um exemplo da estrutura do dicionário.  {'111.222.333-28': 'Paulo', '444.555.234-43': 'Ana', '000.345.543-8':  'João'}

usuarios = {}
for n in range(5):
    cpf = input('insira o seu CPF: ')
    if cpf == '':
        break
    if cpf not in usuarios:
        nome = input('Nome: ')
        usuarios[cpf] = nome                    # insere no dicionário
    else:
        print('O CPF já está cadastrado')
print(usuarios)