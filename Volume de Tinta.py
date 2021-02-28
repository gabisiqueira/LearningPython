import math

area = float(input('Insira a área a ser pintada (m²): '))

# 1L de tinta pinta 3m², portanto, 18L (1 lata de tinta) cobre 54m².
volume_tinta = area / 54
quantidade_latas = math.ceil(volume_tinta)

custo = quantidade_latas * 80

print(f'Serão necessárias {quantidade_latas} latas de tinta no valor de R$ 80.00 cada.')
print(f'O total a ser pago é de R$ {custo:.2f}.')

