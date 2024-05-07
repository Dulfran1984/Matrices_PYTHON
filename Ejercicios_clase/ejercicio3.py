matriz = [['-','-','-'],['-','-','-'],['-','-','-']]
def fnt_agregar(dato, x, y):
    if matriz[x][y] == '-':
        matriz[x][y] = dato.upper()
    elif matriz[x][y] == 'X':
        print('\nEl espacio está ocupado <ENTER>')
def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='     ')
        print()       
sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input('Dato: '),int(input('Fila: ')), int(input('Columna: ')))