notas = []
k = 1
while k <= 5:
    notas.append(float(input('Insira a nota: ')))
    k = k + 1
soma = k = 0
while k < len(notas):
    soma = soma + notas[k]
    k = k + 1
print (f'A média do aluno é {soma/len(notas):.1f}.')

