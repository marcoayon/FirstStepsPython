def calcula_agua(nrodeastonauta,cantidadagua,cantidaddias):
    #Validamos si las variables son númericas
    try:
        for variable in [nrodeastonauta,cantidadagua,cantidaddias]:
            calcula = variable /10 #Uso la operación para validad si es un nro
    except TypeError:
        raise TypeError (f"Todos los argumentos son de tipo número a excepción de {variable}")
    totalaguapordia = nrodeastonauta * 11
    totalagua = totalaguapordia * cantidaddias
    aguanecesaria = cantidadagua - totalagua
    if aguanecesaria < 0:
        raise RuntimeError (f"La cantidad de {cantidadagua} litros de agua para {cantidaddias} días, " 
                            f"es insuficiente para un total de {nrodeastonauta} astronautas.")
    print (f"Después de {cantidaddias} días, quedará un total de {aguanecesaria} litros de agua para {nrodeastonauta} astronautas.")

calcula_agua(2,100,4)
