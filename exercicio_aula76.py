"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


# secreta  = 'python'

# print('Existe uma palavra secreta. Descubra qual é!')
# print('Sempre que uma letra for digitada, ela aparecerá caso esteja presente na \
#     palavra secreta. Caso não, irá aparecer um "*" informando que a letra não faz \
#         parte da palavra secreta. \
#             BOA SORTE!')

# letra = input('Digite uma letra: ').lower()
# verifica  = ''
# tentativas = 0

# while tentativas >= 0:

#     while letra in secreta:
#         verifica += letra
#         tentativas += 1
#         print(letra)
#         print(f'Esta é sua tentativa de número: {tentativas}')

#         letra = input('Digite uma letra: ').lower()
        
#     else:
#         tentativas += 1
#         print('*')
#         print(f'Esta é sua tentativa de número: {tentativas}')
#         letra = input('Digite uma letra: ').lower()

# print(f'Seu número de tentativas foi de {i}X.')

''' Código do professor:
Diferenças importantes: Eu entendi que era para aparecer * quando o usuário erra a letra
Mas era para aparcer a palavras em forma de * e a cada acerto, a letra certa sustituir o *
'''

import os

palavra_secreta = 'perfume'
letra_acertada = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    #verifica se o usuário digitou mais de uma letra:
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    #verifica se a letra digitada está na palavra secreta
    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    #verifica os acertos e retorna a palavra secreta devidamente formatada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    #verifica se o user ganhou o jogo ou não
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCE GANHOU! PARABENS!')
        print('A palavra secreta era: ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        
        #zera o número de tentativas e as letras acertadas:
        letra_acertada = ''
        numero_tentativas = 0

