A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))

while A % B != 0:
    A , B = B, A % B
print(f'MDC: {B}')

