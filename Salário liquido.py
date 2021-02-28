salario_hora = float(input('Insira o valor do salário ganho por hora: '))
horas_trabalhadas_mensais = int(input('Insira a quantidade de horas mensais trabalhadas: '))

salario_bruto = salario_hora * horas_trabalhadas_mensais
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - IR - INSS - sindicato

print(f'Salário bruto mensal: + R$ {salario_bruto:.2f}')
print(f'Valor pago ao IR: - R$ {IR:.2f}')
print(f'Valor pago ao INSS: - R$ {INSS:.2f}')
print(f'Valor pago ao sindicato: - R$ {sindicato:.2f}')
print(f'Salário líquido mensal: + R$ {salario_liquido:.2f}')


