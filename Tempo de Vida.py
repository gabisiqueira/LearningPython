cigarro = int(input('Quantos cigarros diários:'))
anos = float(input('Anos de vida fumante:'))

total_cigarros = anos*360*cigarro
# 1 dia = 1440 minutos / 10 minutos de cada cigarro = 144
dias_perdidos = total_cigarros/144

print(f'Foram perdidos um total de {dias_perdidos} dias de vida')