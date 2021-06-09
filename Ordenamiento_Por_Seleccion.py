def Ordenamiento_Seleccion(arr0):
    arr1 = []
    for a in range(len(arr0)):
        for b in range(len(arr0)-a):
            minimo = min(arr0)
            indice = arr0.index(minimo)
            arr1.append(arr0[indice])
            arr0.remove(arr0[indice])
    print(arr1)
Ordenamiento_Seleccion([2,5,8,3,9,0,1,6,7,5,4,10])