# for i in range(0,3):
#     for j in range(0,3):
#         print(

#         )


# mat =[[1,2],[3,4]]
# print(mat[0][0])

# mat3 = [
#     [0,1,2],
#     [3,4,5],
#     [5,6,7]
# ]

# print(mat3[0][2])
# print(len(mat3))
 
# mat3[0][0] = 93
# print(mat3)

# mat3.append([33,3,423432])
# print(mat3)


print('Programa Matrizes')
print('Informe as dimensões da matriz')
m = int(input('Quantas linhas? '))
n = int(input('Quantas colunas? '))
mat = []
for i in range(m):
    mat.append([])
    for j in range(n):
        v = int(input(f'M[{i}][{j}]: '))
        mat[i].append(v)
print()
print('Matriz lida')
for i in range(m):
    print('|', end='')
    for j in range(n):
        print('%3d'%mat[i][j], end='')
    print(' |')