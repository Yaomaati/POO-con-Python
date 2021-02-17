#En una busqueda binaria lo que haremos es "partir" a la mitad nuestro parametro de busqueda.
#Utilizar éste metodo agiliza la busqueda. Sin embargo ésto hara un mayor uso de la memoria y SOLAMENTE puede usarse en listas ordenadas.
import random



def busqueda_binaria(lista, comienzo, final, objetivo, conteo=0):
    """Reducimos a la mitad el indice de busqueda en cada iteración
    mitad = Asegura la división en enteros del indice
    En cada iteración comparará el número objetivo con la lista. Si es mayor buscará en la mitad superior, si es menor lo hara en la inferior.
    """
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
    conteo += 1
    if comienzo > final:
        return False

    mitad = (comienzo + final) // 2

    if lista[mitad] == objetivo:
        return (True, conteo, 5) #Hay que recordar que ésta función puede devolver mas de 1 valor, y se enlistarán en forma de tupla: (0,1,2,3) y si queremos obtener esos valores adicionales solo debemos solicitarlos en ese mismo orden.
    elif lista[mitad] < objetivo:
        return busqueda_binaria(lista, mitad + 1, final, objetivo, conteo=conteo)
    else:
        return busqueda_binaria(lista, comienzo, mitad - 1, objetivo, conteo=conteo)


if __name__ == "__main__":


    tamano_de_lista = int(input('Introduce el tamaño que la lista en la que deseas buscar: '))
    objetivo = int(input("¿Qué número deseas buscar? "))
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)]) #Crea un for del tamaño de nuestra lista, y en cada iteración genera un número aleatorio entre el 1 y el 99. Y al finál ordena dicha lista
    
    #Recordemos que la función devolvía 2 valores "true" y el resultado de conteo.
    (encontrado, iteraciones, numero_random) = busqueda_binaria(lista, 0, len(lista), objetivo) 
    #(Primer valor devuelvo por la función, segundo valor devuelto por la función, tercer valor devuelto por la función)

    print(lista)
    print(f'Las iteraciones realizadas son: {iteraciones}')
    print(f'El número {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(numero_random)