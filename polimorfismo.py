class Persona: #Declaramos una superclase persona

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('La persona esta caminando')

class Ciclista(Persona): #Subclase ciclista

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en bicicleta')

def main(): #Declaramos una función que utilizará los datos de ambas clases, modificando ligeramente el output en cada caso
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniela')
    ciclista.avanza()


if __name__ == '__main__':
    main() #Esto se entiende como polimorfismo. Donde la "herencia" es tomar metodos de otras clases de manera literal
           #Al hablar de polimorfismo la acción es similar, con la diferencia que modificaremos ligeramente los valores para que se adapten a nuestras necesidades.