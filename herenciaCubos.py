class Puzzles(): #Creamos una clase nueva

    def __init__(self, marca, tipo, precio): #Le damos los valores iniciales
        
        self.marca = marca
        self.tipo = tipo
        self.precio = precio
        self.complejidad_elevada = False
        self.limitado = False
    
    def limitado(self):
        self.limitado = True

    def producto(self): #Utilizamos una función que nos imprima los datos del producto
        print('Marca: ', self.marca, '\nTipo: ', self.tipo, '\nPrecio: ', self.precio, '\nComplejidad elevada: ', self.complejidad_elevada,
                '\nEdición limitada: ', self.limitado)


class Dodecaedro(Puzzles): #Creamos una nueva clase y llamamos a los metodos dentro de la misma, así, aunque  nuestra clase esta "vacía" ha heredado los metodos de la superclase
    pass

nuevo_puzzle = Dodecaedro('Dayan', 'Megaminx', "$520")#Finalmente creamos un nuevo objeto, y lo dotamos de la caracteristicas que solicita la clase.

nuevo_puzzle.producto()#Y aplicamos este metodo sobre nuestro objeto "nuevo_puzzle" para que ejecute el metodo que devolvera a pantalla sus características