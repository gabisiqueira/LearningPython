a = float(input('Insira a dimensão do lado A: '))
b = float(input('Insira a dimensão do lado B: '))
c = float(input('Insira a dimensão do lado C: '))

if a > b + c or b > a + c or c > b + c:
    print ('Não pode ser um triângulo ')
    print ('Um dos lados é maior que a soma dos outros dois')

elif a == b == c:
    print ('É um triângulo equilátero')

elif a == b or b == c or a == c:
    print ("É um triângulo isósceles")

else:
    print ("É um triângulo escaleno")


