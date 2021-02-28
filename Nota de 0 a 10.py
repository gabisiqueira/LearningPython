nota = float(input('Insira uma nota de 0 a 10: '))

if nota < 0 or nota > 10:
    print ('Nota inválida, insira uma nota de 0 a 10.')

else:
    print (f'Nota: {nota:.1f}')

#Outra possibilidade utilizando while:

nota = float(input('Insira uma nota de 0 a 10: '))
while nota < 0 or nota > 10:
    print ('Nota inválida, insira uma nota de 0 a 10.')
    nota = float(input('Insira uma nota de 0 a 10: '))