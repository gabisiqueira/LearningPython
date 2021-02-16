salario = float(input("Insira o valor do salário atual:"))
aumento = float(input("Porcentagem de aumento (%):"))
a = (aumento/100)*salario
ns = salario+a
print (f"Valor do aumento: R$ {a:.2f}")
print (f"Novo salário: R$ {ns:.2f}")
