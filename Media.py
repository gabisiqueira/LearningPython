notas = []
contador = 0
provas = float(input('Insira uma nota: '))
notas.append(provas)
while contador != 4:
    provas = float(input('Insira uma nota: '))
    notas.append(provas)
    contador = contador + 1
soma = 0
k = 0
while k < len(notas):
    soma = soma + notas[k]
    k = k + 1
print (soma/len(notas))
