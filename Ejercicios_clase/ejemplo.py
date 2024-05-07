abecedario1 = [['◉','◉','◉','◉','◉','◉'],
               ['◉','◉','◉','◉','◉','◉'],
               ['◉','◉','◉','◉','◉','◉'],
               ['◉','◉','◉','◉','◉','◉'],
               ['◉','◉','◉','◉','◉','◉']]
abecedario2 = [['A','B','C','D','E','F'],
               ['G','H','I','J','K','L'],
               ['M','N','Ñ','O','P','Q'],
               ['R','S','T','U','V','W'],
               ['X','Y','Z','CH','LL','RR']]
def fnt_limpiar():
    import os
    os.system('cls')
    print('Autor: Dulfran A. Montaño M.')
    print('Lenguaje: Python v 3.12.2 64-bit')
    print('Fecha: 07 de abril del 2024')
    print('\n\n')
    fnt_pintar_matriz()
    print('\n\n')
fila = 0
columna = 0
def fnt_validarPos(dato, x, y):
    global fila
    global columna
    for i in range(len(abecedario2)):
        for j in range(len(abecedario2[i])):
            if abecedario2[i][j] == dato:
                fila = i
                columna = j
                break
    if (x >= 0 and x <= 5) and (y >= 0 and y <= 4):  
        if int(fila) == x and int(columna) == y and dato.upper() == abecedario2[fila][columna]:
            abecedario1[fila][columna] = abecedario2[fila][columna]
            input('\nDato registrado con éxito <ENTER>')
        else:
            input('\nLa posición no coincide <ENTER>')
    else:
        input('\nLa posición no es válida o está fuera de rango <ENTER>')
def fnt_pintar_matriz():
    for i in range(len(abecedario1)):
        for j in range(len(abecedario1[i])):
            print(abecedario1[i][j], end='    ')
        print('\n')
sw = True
while sw == True:
    fnt_limpiar()
    opcion = fnt_validarPos(input('Letra: '), int(input('Fila: ')), int(input('Columna: ')))
