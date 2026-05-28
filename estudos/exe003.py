# Escreva um programa em Python que
# determine se um determinado ano é ou
# não bissexto. Um ano é bissexto quando
# é divisível por 4 e não é divisível por 100,
# ou ainda, quando é divisível por 400.

ano = int(input('digite o ano que você deseja:'))

if (ano % 4 == 0)or (ano % 400 == 0) and (ano % 100 == 1):
    print('e bissexto')
else: 
    print('não é bissexto')