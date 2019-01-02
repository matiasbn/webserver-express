import numpy as np

# matrix es la matriz que se rotara, k es la cantidad de posiciones que se rotara
def clockwiseRotation (matrix,K):
    originalMatrix = np.array(matrix)
    filas=originalMatrix.shape[0]
    columnas=originalMatrix.shape[1]
#Definir matriz de guardado
    saveMatrix = np.zeros((filas,columnas),dtype=int)
#Definir la cantidad de anillos, min(filas,columnas)/2
    ringAmount = min(filas,columnas)/2
#Definir las listas por anillo
    for ring in range (0,ringAmount):
        #------------------------------------------------#
        #GUARDAR ANILLO EN UN ARRAY
        #Arreglo para guardar anillo en array
        ringArray=[[] for l in range(2*filas+2*(columnas-2)-8*ring)]
        #Parametro para guardar en ringArray
        ringParameter = 0
        #J para moverse por columna
        for j in range (0+ring,columnas-ring):
            ringArray[ringParameter]=originalMatrix[ring][j]
            ringParameter+=1
        #K para moverse por fila en la misma columna J 
        for k in range (1+ring,filas-ring):
            ringArray[ringParameter]=originalMatrix[k][j]
            ringParameter+=1
        #L para moverse en la ultima fila del anillo hasta la primera columna
        for l in range (j-1,-1+ring,-1):
            ringArray[ringParameter]=originalMatrix[k][l]
            ringParameter+=1
        #M para moverse por la primera columna hacia arriba
        for m in range (k-1,0+ring,-1):
            ringArray[ringParameter]=originalMatrix[m][l]
            ringParameter+=1
        #------------------------------------------------#
        #DESPLAZAR EL ANILLO EN K POSICIONES   
        #Mover el anillo segun indica k
        ringArray=np.array(ringArray)
        ringArray=np.roll(ringArray,K)
        #------------------------------------------------#
        #GUARDAR ARRAY DESPLAZADO EN MATRIZ AUXILIAR
        #Parametro para guardar en saveMatrix
        saveParameter = 0
        j=k=l=m=0
        #J para moverse por columna
        for j in range (0+ring,columnas-ring):
            saveMatrix[ring][j]=ringArray[saveParameter]
            saveParameter+=1
        #K para moverse por fila en la misma columna J 
        for k in range (1+ring,filas-ring):
            saveMatrix[k][j]=ringArray[saveParameter]
            saveParameter+=1
        #L para moverse en la ultima fila del anillo hasta la primera columna
        for l in range (j-1,-1+ring,-1):
            saveMatrix[k][l]=ringArray[saveParameter]
            saveParameter+=1
        #M para moverse por la primera columna hacia arriba
        for m in range (k-1,0+ring,-1):
            saveMatrix[m][l]=ringArray[saveParameter]
            saveParameter+=1
    #Si es cuadrada impar, guardar el elemento central
    if ((filas == columnas) & (filas%2!=0)):
        saveMatrix[filas/2][columnas/2]=originalMatrix[filas/2][columnas/2]
    return saveMatrix
m = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]).reshape(4,4)
n = np.array([[1,2,3],[4,5,6]]).reshape(2,3)
o = np.arange(25).reshape(5,5)
print o
print clockwiseRotation(o,2)
print '\n'
print m
print clockwiseRotation(m,2)
print '\n'
print n
print clockwiseRotation(n,3)
print '\n'
