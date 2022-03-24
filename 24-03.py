'''
Este programa calcula la tarfia de un estacionamiento en un aeropuerto
'''
tarifa_minima = 1500
ad_x_min = 15
#///////////////////////
tus_horas = int(input('¿Cuantas horas has estado?'))
tus_min = int(tus_horas * 60)
extra = tus_min + ad_x_min
tarfa_despues = tarifa_minima + extra
if tus_horas <=1:
    print('La tarifa de de estacionamiento es:', '$', tarifa_minima )
elif tus_horas >>1:
    print('La tarifa de estacionamiento es:', tarfa_despues)
if tus_horas >> 24:
    print('El maximo de horas las cuales puedes estar en el estacionamineto son 24 horas.')