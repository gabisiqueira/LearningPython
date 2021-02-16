velocidade = int(input('Insira a velocidade: '))
if velocidade > 110:
    print(f'Motorista multado em R$ {(velocidade-110)*5:.2f}')
else:
    print('Motorista dentro do limite de velocidade')
