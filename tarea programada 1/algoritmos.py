def merge_sort(arr, criterio):
    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    merge_sort(izquierda, criterio)
    merge_sort(derecha, criterio)

    i = j = k = 0

    while i < len(izquierda) and j < len(derecha):
        val_izq = izquierda[i].obtener_valor_por_criterio(criterio)
        val_der = derecha[j].obtener_valor_por_criterio(criterio)

        if val_izq < val_der:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1
        k += 1

    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1

    return arr


def quick_sort(arr, criterio):
    if len(arr) <= 1:
        return arr

    pivote_obj = arr[len(arr) // 2]
    pivote_val = pivote_obj.obtener_valor_por_criterio(criterio)

    menores = []
    iguales = []
    mayores = []

    for pokemon in arr:
        val_actual = pokemon.obtener_valor_por_criterio(criterio)
        if val_actual < pivote_val:
            menores.append(pokemon)
        elif val_actual > pivote_val:
            mayores.append(pokemon)
        else:
            iguales.append(pokemon)

    return quick_sort(menores, criterio) + iguales + quick_sort(mayores, criterio)