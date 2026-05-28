# vetor = [14, 37, 18, 92, 77, 64]
# print("Lista original")
# print(vetor)
# vetor[0] = 99
# print("Lista modificada")
# print(vetor)
# print("Elementos individuais")
# print("Valor [0] =", vetor[0])
# print("Valor [1] =", vetor[1])
# print("Valor [2] =", vetor[2])
# print("Valor [3] =", vetor[3])
# print("Valor [4] =", vetor[4])
# print("Valor [5] =", vetor[5])
# print("Valor [6] =", vetor[6])

# mat = [[37, 80, 92], [9, 17, 72], [90, 1, 28]]
# mv = mat[0][0]
# mi = mj = 0
# for i in range(3):
#   for j in range(3):
#     if mat[i][j] < mv:
#       mv = mat[i][j]
#       mi = i
#       mj = j
# print('[', mi, mj, ']')


 
# from random import randint
# mat = [[0,0,0], [0,0,0], [0,0,0]]
# for i in range(3):
#   for j in range(3):
#     if i <= j:
#       mat[i][j] = randint(1,9)
# for i in range(3):
#   for j in range(3):
#     print(mat[i][j], end=' ')
#   print()

# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(3):
#   sm = 0
#   for j in range(3):
#     sm += mat[i][j]
#   print('[', i+1, ']', sm)



# mat1 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# mat2 = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
# print(mat1)
# print(mat2)
# m = len(mat1)
# n = len(mat1[0])
# for i in range(m):
#   for j in range(n):
#     mat2[i][j] = mat1[i][n-j-1]
# print(mat1)
# print(mat2)



# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sd = 0
# for i in range(3):
#   sd = sd + mat[i][i]
#   print(sd)


 
# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# vet = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
# m = len(mat)
# n = len(mat[0])
# for i in range(m):
#   for j in range(n):
#     k = i * n + j 
#     vet[k] = mat[i][j]


# print(vet)
 

# mat = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(3):
#   for j in range(3):
#      mat[i][j] = 3*i+j+1  

# print(mat)
  
# mat = []
# for i in range(3):
#   mat.append([])
#   for j in range(3):
#     mat[i].append(i+j+1)

# print(mat)


# mat = [[],[],[]]
# for i in range(3):
#   for j in range(3):
#     mat[i].append(i*j)

# print(mat)

from random import randint
mat = []
sm = 0
for i in range(3):
  mat.append([])
  for j in range(3):
    val = randint(0,99)
    mat[i].append(val)
    sm += val
print(sm)