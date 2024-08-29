# Exercício 03 
 
# Preencha um dicionário com os dados de 5 alunos.  - Utilize o RM do aluno como chave e uma lista de três notas como valor.  - Solicite os dados ao usuário.  Percorra o dicionário e exiba a média de cada aluno. 
 
# Exemplo:  Veja um exemplo da estrutura do dicionário.  {1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}

alunos = {}

for _ in range (5):
    rm = input('Digite seu rm: ')
    if rm not in alunos:
        notas = []                                        #iniciar a lista dentro do for
        for _ in range(3):
            n = float(input('Digite suas notas: '))
            notas.append(n)
    else: 
        print('RM ja cadastrado!')
        
    media = sum(notas) / 3                                 #soma e calcula a media
    alunos[rm] = notas
    print(alunos)
    print(f'Sua media é {media}')