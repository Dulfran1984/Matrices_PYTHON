matriz = [[0,5,2],[0,3,0],[1,0,4]]
ls_repetir = []
dato = 2
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if dato == matriz[i][j]:
            contador +=1
            pos = 'fila = ',i,' columna: ', j
            ls_repetir.append(pos)
print(f'\nEl {dato} se encuentra {contador} veces')
print(ls_repetir)