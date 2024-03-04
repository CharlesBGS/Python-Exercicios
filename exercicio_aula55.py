"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# entrada = input('Digite um número inteiro: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par =  entrada_int % 2

#     if par == 0:
#         print(f'{entrada} é par.')
#     else:
#         print(f'{entrada} é impar.')
# else:
#     print(f'{entrada} não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Que horas são? ')

# try:
#     hora_int = int(hora)

#     if hora_int <= 11 and hora_int >= 0:
#         print('Bom dia')
    
#     elif hora_int <= 17 and hora_int >= 12:
#         print('Boa tarde')
    
#     elif hora_int <= 23 and hora_int >= 18:
#         print('Boa noite')
    
#     else:
#         print('Não conheço essa hora.')

# except:
#     print('Digite um número inteiro entre 0 e 23.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome  = input('Digite seu primeiro nome: ')
# num_letras_nome = len(nome)

# if num_letras_nome > 1 :

#     if num_letras_nome <= 4:
#         print('Seu nome é curto.')

#     elif num_letras_nome >= 5 and num_letras_nome <= 6:
#         print('Seu nome é normal.')

#     else:
#         print('Seu nome é muito grande.')

# else:
#     print('Digite mais de uma letra.')