a =int(input('digite'))
b =int(input('digite'))
c =int(input('digite'))

if (a <= b) and (b<=c ):
    print('ordem crescente',a,b,c)
if (a <= c) and ( c<=b):
    print('ordem crescente',a,c,b)
if (b<=a) and ( a<=c):
    print('ordem crescente',b,a,c)
if (b<=c) and (c<=a):
    print('ordem crescente',b,c,a)
if (c<=a) and (a<=b):
    print('ordem crescente',c,a,b)
if (c<=b) and (b<=a):
    print('ordem crescente',c,b,a)
    