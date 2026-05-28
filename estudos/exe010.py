# i = 10 

# while i >= 0:
    
#     print(i)
#     i = i -1 

# for i in range(5,0,-1):
#     print(i)

# for i in range(0,20,2):
#     print(i)

# for i in range (40,20,-2):
#     print(i)

# for i in range(11,30,2):
#     print(i)

# for i in range(0,25,4):
#     print(i)


# for i in range(10,20):
#     if i % 2 == 0:
#         print(i)

 
# for i in range(10):
#   print(i+1, end=' ')
# print()


# print("Exibe os divisores de um número")
# num = int(input("Informe número: "))
# for i in range(1,num):
#   if (num % i == 0):
#     print(i, end=' ')
# print()



# print("Soma dos números inteiros entre 1 e 100")
# soma = 0
# for i in range(0,101):   # linha 3
#     soma = i + 1         # linha 4
# print("Soma(1~100) =", soma)


# soma = 0
# for i in range(1, 101): # Linha 3: gera 1 até 100
#     soma += i           # Linha 4: soma o valor atual de i
# print("Soma(1~100) =", soma)


# a = int(input("Valor inicial: "))
# b = int(input("Valor final: "))
# soma = 0
# for i in range(a, b+1):
#   if i % 2 == 1:
#     soma += i
# print("Soma =", soma)

# import random

# print("Jogo do Bicho")
# print("Sorteio do dia:")
# for i in range(5):
#   milhar = random.randint(0, 9999)
#   print("%dº valor: %04d"%(i+1, milhar))



# print("Números da sequência...")
# for i in range(10, 15):
#    print(2*i+1, end=' ')
# print()



# print("Números pares no intervalo 1 a 100")
# for i in range(1,101):        # linha 2    
#    if i % 2 == 0:     # linha 3
#       print(i, end=' ')
# print()



print("Programa Fatorial")        
n = int(input("Valor de n: "))
fact = 1
for i in range(n,1,-1):        # linha 4
   fact = fact * i            # linha 5
print("%d! = %d"%(n, fact))
