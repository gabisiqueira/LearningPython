pais_A = 80000
pais_B = 200000

anos = 0
while pais_A <= pais_B:
    pais_A = pais_A + (pais_A*0.03)
    pais_B = pais_B + (pais_B*0.015)
    anos = anos + 1

print(f'Serão necessários {anos} anos para o país A ultrapassar o país B em número de habitantes.')

