# """
# Iterando strings com while
# """
# #       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string = ''
# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

# Minha tentativa:

# nome = 'Luiz Otávio'
# nome_editado = 0
# tamanho_nome = len(nome)
# contador =  0
# fatiamento_inicio = 0
# fatiamento_fim = tamanho_nome
# separador  = '*'

# while contador != tamanho_nome:
    
#     print(nome_editado)
#     contador += 1
#     fatiamento_fim -= 1
#     nome_editado = nome[fatiamento_inicio:fatiamento_fim]

#     print(separador, nome_editado, separador)


# print(nome_editado)


# Resolucao do professor:

nome = 'Luiz Otávio'
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)