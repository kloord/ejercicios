'''
Calcula el valor de un menu en un local de comida
'''


big_whop = int(3500)
cajitaJR = int(2500)
papas_fritas = int(800)
bebidas = int(1000)
print('Bienvendo a McKing, nustro menú es el siguente:')
print('Big Whop = 3500 pesos')
print('Cajita Jr = 2500 pesos')
print('Papas Fritas = 800 pesos')
print('Bebidas = 1000 pesos')
cts_big_whop = int(input('¿Cuantas Big Whoper deesea llevar?: '))
cts_catiasJr = int(input('¿Cuantas Cajitas Jr desea llevar?: '))
cts_papas = int(input('¿Cuantas papas fritas desea llavar?: '))
cts_bebidas = int(input('¿Cuantas bebidas desea llevar?: '))

precio_bw = big_whop * cts_big_whop
preciocJR = cajitaJR * cts_catiasJr
precio_pf = papas_fritas * cts_papas
precio_beb = bebidas * cts_bebidas

total_productos = int(cts_big_whop + cts_catiasJr +cts_papas + cts_bebidas)
precio_parcial = int(precio_bw + preciocJR + precio_pf + precio_beb)

if precio_parcial > 10000 and total_productos < 7:
    print('El costo total del producto es de ', precio_parcial, ',', 'y el costo de envío es de 0 pesos.', 'El costo total de su compra es de', precio_parcial + 0, ' pesos'  )
elif precio_parcial > 10000 and total_productos >= 7:
    print('El costo total del producto es de ', precio_parcial, ',', 'y el costo de envío es de 1000 pesos.', 'El costo total de su compra es de', precio_parcial + 1000, ' pesos')
else:
    print('El costo total del producto es de ', precio_parcial, ',', 'y el costo de envío es de 2000 pesos.', 'El costo total de su compra es de ', precio_parcial + 2000, ' pesos')