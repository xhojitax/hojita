import datetime

fecha_hora = datetime.datetime.now()
formato_personalizado = "%Y-%m-%d %h:%M:%S"
fecha_hora_form = fecha_hora.strftime(formato_personalizado)

import json

ventas=[]

precio_pizzas={
    'peperoni':{'pequeña': 5000, 'mediana': 8000, 'familiar': 10000},
    'mediterranea':{'pequeña': 6000, 'mediana': 9000, 'familiar': 12000},
    'vegetariana':{'pequeña': 5500, 'mediana': 8500, 'familiar': 11000}
}

def menu():
    print('\n--- Sistema de ventas de pizza Duoc---')
    print('1. Registrar una venta')
    print('2. Mostrar todas las ventas.')
    print('3. Buscar ventas por cliente')
    print('4. Guardar ventas en un archivo.')
    print('5. Cargar las ventas desde un archivo')
    print('6. Generar boleta.')
    print('7. Salir del programa')
    

def registrar_ventas():
    cliente=input('ingrese el nombre del cliente: ').lower()
    tipo_cliente=input('ingrese el tipo de cliente: ').lower()
    tipo_pizza=input(' ingrese tipo de pizza: ').lower()
    tamaño_pizza=input('ingrese el tamaño de la pizza: ').lower()
    cantidad=int(input('ingrese la cantidad de pizzas: '))
    
    
    precio_unitario = precio_pizzas[tipo_pizza][tamaño_pizza]
        
    descuento=0
    
    if tipo_cliente == 'diurno':
        descuento= 0.15
    elif tipo_cliente == 'vespertino':
        descuento = 0.20
    elif tipo_cliente == 'administrativo':
        descuento = 0.10
        
    precio_total= precio_unitario * cantidad
    precio_final= precio_total * (1 - descuento)

#registro de la venta
    venta = {
        'cliente': cliente,
        'tipo_cliente': tipo_cliente,
        'tipo_pizza': tipo_pizza,
        'tamaño_pizza': tamaño_pizza,
        'cantidad': cantidad,
        'precio_final': precio_final
    }
    ventas.append(venta)
    print('venta registrada exitosamente')
    
#mostrar venta    
def mostrar_ventas():
    for venta in ventas():
        print(venta)

#buscar ventas       
def buscar_venta_cliente():
    buscar_cliente= input('ingrese el nombre del cliente: ').lower()
    ventas_encontradas=[venta for venta in ventas if venta['cliente']== buscar_cliente]
    
    if ventas_encontradas:
        for venta in ventas_encontradas:
            print(venta)
    else:
        print(f'no se encontraron ventas {buscar_cliente}')

def guardar_venta():
    with open('ventas.json', 'w') as archivo:
        json.dump(ventas, archivo)
    print('ventas guardadas con exito.')

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r') as archivo:
            ventas= json.load(archivo)
        print('ventas guardadas en archivo ventas')
    except FileNotFoundError:
        print('no se encontro el archivo ventas')

def generar_boleta():
    cliente = input('ingrese nombre del cliente: ')
    ventas_cliente=[venta for venta in ventas if venta['cliente']== cliente]
    if ventas_cliente:
        total= sum(venta['precio_final'] for venta in ventas_cliente)
        print('\nBoleta: ')
        print(f'cliente: {cliente}')
        print(f'fecha: {datetime.datetime.now()}')
        print('Detalle de compras: ')
        for venta in ventas_cliente:
            print(f"{venta['tipo_pizza']} - {venta['tamaño_pizza']} - ${venta['precio_final']}")
            print(f'Total a pagar: ${total}\n')
    else:
        print('no se encontraron ventas para ese cliente.')
    
while True:
    menu()
    op=input('Seleccione una opcion: ')

    if op == '1':
        registrar_ventas()
    elif op =='2':
        mostrar_ventas()
    elif op == '3':
        buscar_venta_cliente()
    elif op == '4':
        guardar_venta()
    elif op == '5':
        cargar_ventas()
    elif op == '6':
        generar_boleta()
    elif op == '7':
        print('Saliendo del Probrama.')
        break
    else:
        print('opcion no valida.')