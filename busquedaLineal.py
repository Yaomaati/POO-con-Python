import random

def busqueda_lineal(lista, objetivo): #Creamos una función que iteré en una lista determinada y devuelva un valor de True o False en caso de encontrar el número buscado

    match = False

    for i in lista:
        if i == objetivo:
            match = True
            break #Si el número se encuentra en la lista la busqueda se detendrá (Hay que recordar que éste tipo de busqueda es eficiente en busquedas pequeñas, cuanto mas grande sea la busqueda será menos eficiente, pero no obsoleto)
            
            return match

if __name__ == '__main__':
    tamaño_lista = int(input('¿De qué tamaño deseas que sea la lista? '))
    objetivo = int(input('¿Qué elemento deseas encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamaño_lista)] #Generamos números aleatorios y agregamos uno por cada iteración. El número de iteraciones los dará el usuario
    encontrado = busqueda_lineal(lista, objetivo) #Creamos una variable que tome el valor devuelto por nuestra función "True" o "False"

    print(lista) #Mostramos la lista en pantalla para que el usuario verifique el resultado
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    #Y por último imprimimos el número que el usuario nos solicitó, y a través de una condicional elegimos el tipo de mensaje que será enviado a pantalla.