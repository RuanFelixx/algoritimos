# # Escreva um programa em Python que
# # leia a data de nascimento de um
# # usuário, obtenha a data atual do
# # sistema e calcule, exatamente, quantos
# # anos ele possui, verificando se o usuário
# # já completou ou não aniversário no ano
# # atual.

# from datetime import date
# hoje = date.today()
# ano_atual = hoje.year
# mes_atual = hoje.month
# dia_atual = hoje.day

# ano = int(input('digie o ano que você nasceu:'))
# mes = int(input('digite o seu mês:'))
# dia = int(input('digite o dia:'))

# dif_ano = ano_atual - ano
# dif_mes = mes_atual - mes
# dif_dia = dia_atual - dia
# if (dif_ano and dif_mes and dif_dia) > hoje:
#     print('você ja completou ano')
#     print(f'você tem anos{dif_ano}, {dif_mes} meses e {dif_dia} dias')
# else:
#     print('você não completou ano')
#     print(f'você tem anos{dif_ano}, {dif_mes} meses e {dif_dia} dias')


from datetime import date


hoje = date.today()
ano_atual = hoje.year
mes_atual = hoje.month
dia_atual = hoje.day


ano = int(input('Digite o ano que você nasceu (AAAA): '))
mes = int(input('Digite o mês (1-12): '))
dia = int(input('Digite o dia: '))

# 3. Calcular a idade baseada apenas nos anos
idade = ano_atual - ano

# 4. Verificar se o aniversário já ocorreu este ano
# Compara (mês, dia) atual com (mês, dia) de nascimento
if (mes_atual, dia_atual) < (mes, dia):
    idade -= 1  # Ainda não fez aniversário, subtrai 1 ano
    ja_fez = False
else:
    ja_fez = True

# 5. Exibir resultado
print("-" * 30)
if ja_fez:
    print(f'Você já fez aniversário este ano.')
else:
    print(f'Você ainda não fez aniversário este ano.')

print(f'Sua idade exata é: {idade} anos.')
print("-" * 30)
