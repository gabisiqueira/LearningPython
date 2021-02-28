# A cada quilo de peixe ultrapassado do limite de 50 kg, deverá ser paga uma multa de R$4,00 por quilo excedido.
peso = float (input('Insira o peso do peixe: '))
excesso = peso - 50
multa =  excesso * 4
if peso > 50:
     print (f'Peso excedido em {excesso} kgs.')
     print (f'Multado no valor de R$ {multa:.2f}')
else:
    print ('Peso dentro do limite')