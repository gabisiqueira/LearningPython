a = float (input('Insira o primeiro número: '))
b = float (input('Insira o segundo número: '))
c = float (input('Insira o terceiro número: '))

if a >= b and a >= c:
    print (f'{a} é o maior número')
elif b >= c:
    print (f'{b} é o maior número')
else:
    print (f'{c} é o maior número')

if a <= b and a <= c:
    print (f'{a} é o menor número')
elif b <= c:
    print (f'{b} é o menor número')
else:
    print (f'{c} é o menor número')

