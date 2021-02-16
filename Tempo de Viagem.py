import math

d = float(input('Distância (KM):'))
vm = float(input('Velocidade Média(KM/h):'))
m, h = math.modf(d/vm)
minutos = m*60
print(f'{h:.0f} horas e {minutos:.0f} minutos até o destino')             
