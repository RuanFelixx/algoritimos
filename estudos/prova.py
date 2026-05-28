# lista = [22, 3, 7, 48, 42]
# print('Lista Inicial:',lista)
# tam = len(lista)
# for i in range(tam-1):
#     for j in range(i+1,tam):
#         if lista[i] > lista[j]:
#             aux = lista[i]
#             lista[i] = lista[j]
#             lista[j] = aux
#             print('i=%d, j=%d, Lista: '%(i,j),lista)
# print('Lista Final:',lista)










# k = int(input("Digite a quantidade de alunos na turma (k): "))

# idades = []
# print(f"Digite as {k} idades:")
# for i in range(k):
#     idade = int(input(f"Idade do aluno {i+1}: "))
#     idades.append(idade)

# idades.sort()

# print("\n--- Resultados Estatísticos ---")
# print(f"Turma ordenada: {idades}")

# media = sum(idades) / k

# frequencias = {}
# for idade in idades:
#     if idade in frequencias:
#         frequencias[idade] += 1
#     else:
#         frequencias[idade] = 1


# maior_frequencia = max(frequencias.values())


# modas = []
# for idade, freq in frequencias.items():
#     if freq == maior_frequencia:
#         modas.append(idade)


# if k % 2 != 0:
#     # Se o número de elementos for ímpar
#     mediana = idades[k // 2]
# else:
#     # Se o número de elementos for par
#     pos1 = idades[(k // 2) - 1]
#     pos2 = idades[k // 2]
#     mediana = (pos1 + pos2) / 2

# amplitude = max(idades) - min(idades)


# print(f"Média: {media:.2f}")
# print(f"Moda(s): {modas}")
# print(f"Mediana: {mediana}")
# print(f"Amplitude: {amplitude}")







clientes = []

nome_tutor = input("Informe o nome do tutor: ")
pet = input("Informe o nome do pet: ")
tipo = input("Informe a espécie (Cão/Gato/Ave/Outro): ")
sexo = input("Informe o sexo do pet (M/F): ")
idade = input("Informe a idade do pet (em anos): ")
cidade = input("Informe a cidade de residência: ")
estado = input("Informe o estado de residência (UF): ")
clientes += [nome_tutor, pet, tipo, sexo, idade, cidade, estado]


total_pets = 0
machos = 0
femeas = 0

# Caminha de 7 em 7 para analisar cada pet individualmente
for i in range(0, len(clientes), 7):
    sexo = clientes[i + 3]
    total_pets += 1
    
    if sexo.upper() == 'M':
        machos += 1
    elif sexo.upper() == 'F':
        femeas += 1

print("--- RELATÓRIO DE GÊNERO DOS PETS ---")
if total_pets > 0:
    perc_machos = (machos / total_pets) * 100
    perc_femeas = (femeas / total_pets) * 100
    print(f"Total de animais cadastrados: {total_pets}")
    print(f"Sexo Masculino: {perc_machos:.2f}%")
# Caminha de 7 em 7 para analisar cada pet individualmente
for i in range(0, len(clientes), 7):
    sexo 
    print(f"Sexo Feminino: {perc_femeas:.2f}%")
else:
    print("Nenhum cliente cadastrado na base de dados.")




print("--- RELATÓRIO: CÃES IDOSOS (10+ ANOS) ---")
encontrou_caes = False

for i in range(0, len(clientes), 7):
    tutor = clientes[i]
    pet = clientes[i + 1]
    tipo = clientes[i + 2]
    idade = int(clientes[i + 4]) # Convertendo a string para inteiro para comparar
    
    # Filtro: Tipo Cão (ignorando maiúsculas/minúsculas) e Idade >= 10
    if tipo.lower() == 'cão' or tipo.lower() == 'cao' and idade >= 10:
        print(f"Tutor: {tutor} | Pet: {pet} (Idade: {idade} anos)")
        encontrou_caes = True

if not entrou_caes:
    print("Nenhum cão com 10 anos ou mais foi encontrado.")


print("--- BUSCA DE CIDADES POR ESTADO ---")
uf_busca = input("Informe a sigla do estado (UF) para busca: ").upper().strip()

# Usamos um set para garantir que as cidades não sejam duplicadas no relatório
cidades_encontradas = set()

for i in range(0, len(clientes), 7):
    cidade = clientes[i + 5]
    estado = clientes[i + 6]
    
    if estado.upper().strip() == uf_busca:
        cidades_encontradas.add(cidade.title()) # Padroniza com a primeira letra maiúscula

print(f"\nCidades com clientes atendidos em {uf_busca}:")
if cidades_encontradas:
    for cidade in sorted(cidades_encontradas): # Exibe em ordem alfabética
        print(f"- {cidade}")
else:
    print(f"Nenhum cliente cadastrado no estado {uf_busca}.")