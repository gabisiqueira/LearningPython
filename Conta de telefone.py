minutos_ligacao = int(input('Minutos de ligação mensais: '))
if minutos_ligacao < 200:
    conta_menor_200 = minutos_ligacao*0.2
    print(f'O valor da conta de telefone é de R$ {conta_menor_200}')
else:
    if minutos_ligacao <= 400:
        conta_menor_igual_400 = minutos_ligacao*0.18
        print(f'O valor da conta de telefone é de R$ {conta_menor_igual_400}')
    else:
        conta_maior_400 = minutos_ligacao*0.15
        print(f'O valor da conta de telefone é de R$ {conta_maior_400}')