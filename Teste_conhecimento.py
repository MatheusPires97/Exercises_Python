"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if nome and idade:
    print(f'seu nome é {nome}')
    
    print(f'seu nome invertido é {nome[::-1]}')
    
    if ' ' in nome:
        print('Seu nome contém espaço')
    
    else:
        print('Seu nome não contem espaço')
    
    print(f'Seu nome contem {len(nome)} letras')
    
    print(f'A primeira letra do seu nome é {nome[0]}')
    
    print(f'A ultima letra do seu nome é {nome[-1]}')
    
    print(f'A sua idade é {idade} anos')

    if idade > 10 and idade < 13:
        print('Você é um(a) pré adolescente')

    elif idade > 12 and idade < 18:
        print('Você é um(a) adolescente')

    elif idade >= 18 and idade < 60:
        print('Você é adulto(a)')
    
    elif idade >= 60:
        print('Você é idoso(a)')

    else:
        print('Você é criança')

else:
    print('Desculpe, você deixou os campos vazios.')
