class Coordenada:  #Una clase puede considerarse un "molde" para crear diferentes objetos, la clase debe ser creada con mayúscula inicial.

        def __init__(self, x, y): #Se definen los parametros y se utiliza "self" para definir la instancia (objeto nuevo) esta llamando a parametros de sí misma, y nombramos a dichos parametros
        
            self.x = x #Se retoma el nombre de los parametros que declaramos anteriormente
            self.y = y #Y se les asigna una variable, con el mismo nombre que guarde los datosk, que en éste caso serían las coordenadas

        def distancia(self, otra_coordenada): #Creamos otra instancia que será la encargada de guardar los siguientes parametros
            x_diff = (self.x - otra_coordenada.x) 
            y_diff = (self.y - otra_coordenada.y) 

            return (x_diff**2 + y_diff**2)**0.5 #En éste pundo únicamente devolvemos la operación correspondiente para determinar la distancia entre los puntos.
        


if __name__ == "__main__":
    coord_1 = Coordenada(1 ,  1) #Creamos un objeto utilizando la clase "Coordenada" y añadimos los valores iniciales
    coord_2 = Coordenada(5, 10) #Creamos un segundo objeto que será nuestro punto 2 dentro de la operación.

    print(f'La distancia es: {coord_1.distancia(coord_2)}')  #utilizando el primer objeto, llamamos al metodo "distancia" que creamos previamente, y le pedimos que realicé la operación dandole como parametros nuestro segundo objeto creado.
