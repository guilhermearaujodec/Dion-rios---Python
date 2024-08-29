# Exercício 04 
 
# Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é 
# a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto. 
 
# Exemplo:  Para o texto abaixo:  'faculdade de tecnologia fiap'  A função deve retornar o seguinte dicionário:  {'a': 4, 'u': 1, 'e': 3, 'o': 2, 'i': 2}



def contvogais(texto) -> None:
    
    vogais = {}
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    for x in texto:
        if x == 'a':
            a += 1
            vogais['a'] = a
            
        elif x == 'e':
            e += 1
            vogais['e'] = e
            
        elif x == 'i':
            i += 1
            vogais['i'] = i
            
        elif x == 'o':
            o += 1
            vogais['o'] = o
            
        elif x == 'u':
            u += 1
            vogais['u'] = u
            
        else:
            cons = 0
            cons += 1
            
    print(vogais)
    
texto = input('Digite o texto: ')
contvogais(texto)