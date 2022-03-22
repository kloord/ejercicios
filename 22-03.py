'''
Calcula el IMC
'''
peso = float(input('Cual es tu peso?'))
estatura = float(input('Cual es tu estatura?'))
altura_c = estatura * estatura
imc = float(peso / altura_c)
if imc < 18.5:
    print('Tu IMC es', imc, 'y tu indice de peso es bajo')
elif imc <= 24.9:
    print('Tu IMC es', imc, 'y tu indice de peso es normal')
elif imc <= 29.9:
    print('Tu IMC es', imc, 'y tu indice de peso es sobrepeso')
elif imc >= 30.0:
    print('Tu IMC es', imc, 'y tu indice de peso es sobrepeso')
