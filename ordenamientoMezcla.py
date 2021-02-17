import random

def merge_sort(lista):
    """Realizamos un ordenamiento mezclado (merge_sort)
    Dividimos de manera recursiva la lista principal, hasta convertir cada elemento en una lista.
    Posteriormente se ordena y reintegra cada componente a una nueva lista ordenada.
    """
    if len(lista) > 1: #Nos aseguramos de que la función solamente realice la acción en listas con mas de 2 componentes
        mitad = len(lista) // 2 #Dividimos en 2 la lista
    
        primera_mitad = lista[:mitad] #Creamos otra lista con la primera parte de esa división
        segunda_mitad = lista[mitad:] #Y hacemos lo propio con la segunda

        merge_sort(primera_mitad) #Despues hacemos que el programa repita el proceso continuamente sobre si mismo.
        merge_sort(segunda_mitad) #De modo que al final haya varias listas, con un solo elemento cada una.

        i = 0
        j = 0
        k = 0

        while i < len(primera_mitad) and j < len(segunda_mitad): 
            if primera_mitad[i] < segunda_mitad[j]:
                lista[k] = primera_mitad[i]
                i += 1
            else: 
                lista[k] = segunda_mitad[j]
                j += 1
            k += 1

        while i < len(primera_mitad):
            lista[k] = primera_mitad[i]
            i += 1
            k += 1

        while j < len(segunda_mitad):
            lista[k] = segunda_mitad[j]
            j += 1
            k += 1

if __name__ == '__main__':
    tamano_lista = int(input('¿De que tamaño deseas que sea tu lista? '))
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)

    merge_sort(lista)
    print(lista)