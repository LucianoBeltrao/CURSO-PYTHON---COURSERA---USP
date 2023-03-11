def remove_repetidos(lista):
    lista2=[]
    for objeto in lista:
        if objeto in lista2:
            del objeto
        else:
            lista2.append(objeto)
    lista2.sort()
    return lista2
    
