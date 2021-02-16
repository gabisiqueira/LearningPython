km = float(input('Insira a quilometragem rodada:'))
dias = int(input('Quantidades de dias alugado:'))
preço = (60*dias)+(km*0.15)

print(f'O valor a ser pago é de R$ {preço} por {dias} dias de aluguel e {km} quilometros rodados')