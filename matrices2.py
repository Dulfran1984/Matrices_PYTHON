import os
matriz = [[0,0,0],[0,0,0],[0,0,0]]
filas = 0
columnas = 0
def fnt_limpiar():
    os.system('cls')
    print('Autor: Dulfran A. Montaño M.')
    print('Semestre: I')
    print('Asignatura: ALGORITMICA Y LOGICA DE PROGRAMACION')
    print('Lenguaje de programación: Python')
    print('\n\n')
    fnt_mostrar_matriz()
    print('\n\n')
def fnt_mostrar_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='    ')
        print('\n')
def fnt_agregar_elemento(dato):
    global filas
    global columnas
    fnt_limpiar()
    if dato == '':
        input('\nDebe ingresar un dato <ENTER>')
    else:
        if filas == 3:
            input('\nLa matriz está llena <ENTER>')
        else:
            if filas <= 2:
                matriz[filas][columnas] = dato
                columnas += 1
                input(f'\nEl dato {dato} ha sido registrado con éxito <ENTER>')
            if columnas == 3:
                filas += 1
                columnas = 0
def fnt_numero_repetido(dato):
    fnt_limpiar()
    global contador
    contador = 0
    sw = False
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == dato:
                contador +=1
    
    input(f'\nEl número {dato} se repite {contador} veces dentro de la matriz <ENTER>')        
sw = True
while sw == True:
    fnt_limpiar()
    opciones = input('<<< MENÚ DE OPCIONES >>>\n\n1. AGREGAR ELEMENTO\n2. NÚMERO REPETIDO\n3. SALIR\n\n- >  ')
    if opciones == '1':
        fnt_agregar_elemento(int(input('\nIngresa el número a agregar - >  ')))
    elif opciones == '2':
        fnt_numero_repetido(int(input('\nIngresa el número a buscar - >  ')))
    elif opciones == '3':
        input('\nFin del programa <ENTER>')
        sw = False
    else:
        input('\nIngresa una opción válida <ENTER>')