class Rectangulo():#Creamos una clase

    def __init__(self, base, altura): #Inicializamos el constructor

        #Definimos variables de instancia
        self.base = base
        self.altura = altura

    def area(self): #Definimos la instancia que devolvera la operación deseada
        return self.base * self.altura


class Cuadrado(Rectangulo): #Creamos una subclase

    def __init__(self, lado): #Inicializamos el constructor
        super().__init__(lado, lado)  #Utilizamos la función "super" la cuál nos dará una referencia de la superclase, que en éste claso es el Rectangulo
                                      #Notese como aquí estamos indicando que los parametros de "__init__" de rectangulo, serán sustituidos o "llenados" por los parametros del "__init__" de nuestra subclase
                                      #Es decir, indicaremos que tanto la base como la altura usaran como parametro nuestra variable "lado"

if __name__ == '__main__':
    cuadrado = Cuadrado(lado=4)
    print(cuadrado.area())                                  