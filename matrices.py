#paso 1: instalar pip install numpy
#paso 2: ir al siguiente enlace: 
'''matriz = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]'''#declarando la matriz

'''for i in range(len(matriz)):#Mostrar matriz de forma filas y columnas
    for j in range(len(matriz[i])):
        print(matriz[i][j], end='  ')
    print('\n')
    
print(matriz)#Impresión de forma lineal'''

#Ingresando datos a la matriz con ciclo
'''for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f'Ingrese el valor de la posición [{i}][{j}]: '))
print(matriz)'''

#ingresando datos de manera manual
sw = True
filas = 0
columnas = 0
contador = 0
import os
matriz = [['-','-','-'],['-','-','-'],['-','-','-']]
def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='    ')
        print('\n')
while sw == True:
    os.system('cls')
    print('Cantidad de datos ingresados - >  ', contador)
    print('\nFilas...... ', filas)
    print('Columnas... ', columnas)
    print('\n\n')
    fnt_impresion_matriz()
    opcion = input('\n\n<<< MENÚ PRINCIPAL >>>\n\n1. AGREGAR\n2. MOSTRAR\n3. CONSULTAR\n4. SALIR\n- >  ')
    if opcion == '1':
        if filas == 3:
            input('\nLa matriz está llena <ENTER>')
        else:
            if filas <= 2:
                valor = input('\nIngrese un nombre - > ')
                contador+=1
                matriz[filas][columnas] = valor
                columnas += 1
            if columnas == 3:
                filas += 1
                columnas = 0
    if opcion == '2':
        os.system('cls')
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                print(matriz[i][j], end='  ')
            print('\n')
        input('\nFin del registro <ENTER>')
    if opcion == '3':
        sw2 = False
        os.system('cls')
        buscar = input('\nIngrese el nombre a buscar - > ')
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == buscar:
                    sw2 = True
        if sw2 == True:
            input(f'\nEl nombre {buscar} se encuentra registrado <ENTER>')
        else:
            input(f'\nEl nombre {buscar} no se encuentra registrado <ENTER>')
    if opcion == '4':
        input('\nFin del programa <ENTER>')
        sw = False