mat = []

lin = int(input('digite a quantidade de linhas:'))
col = int(input('digite a quantidade de colunas:'))

for i in range(0,lin):
    oumat = []
    mat.append(oumat)

    for j in range(0,col):
        num = int(input('digite um valor num:'))
        oumat.append(num)

lmat = []

lin = int(input('digite a quantidade delinhas da mat:'))
col = int(input('digite a quantidade de colunas da matriz:'))

for i in range(0,lin):
    jmat = []
    lmat.append(jmat)
    for j in range(0,col):
        num = int(input('digite outros numeros:'))
        jmat.append(num)

print(mat)
print(lmat)

soma_mat = []

for i in range(len(mat)):
    new_mat = []
    soma_mat.append(new_mat)
    for j in range(len(lmat)):
        resultado = mat[i][j] + lmat[i][j]
        new_mat.append(resultado)

print(soma_mat)

