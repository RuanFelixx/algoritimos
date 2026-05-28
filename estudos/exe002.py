# Escreva um programa em Python que
# leia os nomes e as idades de dois
# usuários. O programa deve calcular e
# exibir na tela a diferença de idade entre
# eles. Independente da ordem em que os
# dados forem digitados, a diferença entre
# as idades deve ser exibida sempre como
# um valor positivo

pri_nome = str(input('digite seu nome:'))
pri_idade = int(input('digite sua idade:'))

seg_nome = str(input('digite o nome do segundo usuario:'))
seg_idade = int(input('digite a idade do segundo usuario:'))

pri_dife = pri_idade - seg_idade
seg_dife = seg_idade - pri_idade

if pri_idade > seg_idade:
    print('a diferença entre as idades é',pri_dife)

elif pri_idade < seg_idade:
    print('a diferença entre as idades é:',seg_dife)
    
else:
    print('idades iguais')