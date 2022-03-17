'''
El programa dice tu peso en marte
'''
peso = float(input('Cual es tu peso:'))
print('Tu peso en la tierra es ', int(peso), 'kg')
#gravedad_en_marte = 3.7
#gravedad_en_la_tierra =9.8
peso_en_marte = round(peso * 3.7/ 9.8)
print('Tu peso redondeado en Marte es:', peso_en_marte, 'kg')
