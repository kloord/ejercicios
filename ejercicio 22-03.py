'''
Este programa te genera una contraseña
'''
name =str(input('¿Cual es tu nombre?'))
last_name =str(input('¿Cual es tu apellido?'))
cant_de_sonrisas = int(input('¿Cual es la cantidad de sonrisas en las que te quieres clasificar?'))
longitud_nomap = len(name) + len(last_name)
sonrisas = ';)' * cant_de_sonrisas
nombre_mayus = name.upper() + ' ' + last_name.upper()
password = name.capitalize() + '.' + last_name.capitalize() + '#'
passcompleta = password + str(longitud_nomap)
print(f"\n Felicitaciones {nombre_mayus}, tu contraseña es {passcompleta} {sonrisas}")





