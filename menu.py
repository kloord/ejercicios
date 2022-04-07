
menu=0 #permite ingresar al while la primera
menu_2 = 0
while menu!=4:

    print( )
    print("1. Pedir un prestamo")
    print("2. Realizar depósito")
    print("3. Transformar monedas internacionales")
    print("4. Salir")
    print(' ')
    menu=int(input("Por favor, ingresar una opción: "))


    if menu==1:
        #variables
        ingreso=int(input("Favor de ingresar su ingreso mensual: "))
        anos=int(input("Ingrese su año de nacimiento: "))
        n_hijos=int(input("Ingrese la cantidad de hijo que tenga: "))
        anos_banco=int(input("Ingrese años que pertenece usted al banco: "))
        estado_civil=str(input("Intrese su estado civil (S, soltero / C, casado): "))
        vivienda=str(input("Ingrese tipo de recidencia (U, urbano / R, rural): "))

        if anos_banco >= 10 and n_hijos >= 2:
            print()
            print("APROBADO")
            print()
        elif estado_civil == "C" and n_hijos > 3 and anos >= 1967 and anos <= 1977:
            print()
            print("APROBADO")
            print()
        elif ingreso >= 2500000 and estado_civil == 'S' and vivienda == 'U':
            print()
            print("APROBADO")
            print()
        elif ingreso >= 3500000 and anos_banco >= 5:
            print()
            print("APROBADO")
            print()
        elif n_hijos <= 2 and estado_civil == 'C' and vivienda == 'R':
            print()
            print("APROBADO")
            print()
        else:
            print()
            print("RECHAZADO")
            print()
    if menu==3:
            clp = float(input('Ingresa tu monto en pesos chilenos: '))
            dolar_a = float(round(clp / 787.41, 2))
            dolar_c = float(round(clp / 630.20, 2))
            euro = float(round(clp / 857.85, 2))
            yenes = float(round(clp / 6.35, 2))
            rupias = float(round(clp / 10.43, 2))
            print('Tu monto convertido a dolar estadounidense es ', dolar_a, 'USD')
            print('Tu monto convertido a dolar canadiense es ', dolar_c, 'CAD')
            print('Tu monto convertido a euro es ', euro, '€')
            print('Tu monto convertido a yenes es ', yenes, '¥')
            print('Tu monto convertido a rupias es ', rupias, 'Rs')
    if menu == 2:
        deposito = True
        contar = 0
        sumar = 0
        while deposito:
            deposito = int(input('Ingrese el monto que desea depositar en pesos chilenos: '))
            contar = contar + 1
            sumar = sumar + deposito
            if deposito == 0:
                contar = contar-1
                deposito = False
        print( )
        print('Monto depositado: ', sumar, 'pesos' )
        print ('Cantidad de depositos: ', contar,)  
        print( )