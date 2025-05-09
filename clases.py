# ==============================
# CLASES EN PYTHON
# ==============================

"""
¿Qué es una clase?
------------------
Una clase es como un "molde" o "plantilla" que nos permite crear objetos con características
y comportamientos similares. Por ejemplo, si pensamos en gatos:
- Todos los gatos tienen nombre, color y edad (características/atributos)
- Todos los gatos pueden comer, dormir y hacer sus necesidades (comportamientos/métodos)

¿Qué es self?
-------------
'self' es una referencia al propio objeto que estamos creando. Es como decir "yo mismo".
Cuando usamos 'self.nombre', estamos diciendo "mi nombre". Es obligatorio usarlo como
primer parámetro en los métodos de la clase.

Ventajas de usar clases:
------------------------
1. Reutilización de código: Define una vez, usa muchas veces
2. Organización: Mantiene junto el código relacionado
3. Encapsulamiento: Protege los datos y funciones
4. Herencia: Permite crear nuevas clases basadas en existentes
5. Representación del mundo real: Modela objetos y conceptos reales
"""


class Gatos:
    """
    Clase que representa a un gato y sus comportamientos básicos.

    Atributos:
        nombre (str): Nombre del gato
        color (str): Color del pelaje del gato
        edad (int): Edad del gato en años
    """

    def __init__(self, nombre="", color="", edad=0):
        """
        Constructor de la clase Gatos.
        Este método se llama automáticamente al crear un nuevo gato.

        Args:
            nombre (str): Nombre del gato
            color (str): Color del pelaje
            edad (int): Edad en años
        """
        # self.nombre significa "mi nombre", guardamos el valor en el objeto
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def comer(self):
        """Simula el comportamiento de comer del gato."""
        print(f"{self.nombre} está comiendo su comida")

    def dormir(self):
        """Simula el comportamiento de dormir del gato."""
        print(f"{self.nombre} está durmiendo plácidamente")

    def hacer_necesidades(self):
        """Simula el comportamiento de hacer necesidades del gato."""
        print(f"{self.nombre} está usando su caja de arena")

    def presentarse(self):
        """Método que hace que el gato se presente."""
        print(
            f"""
        ¡Miau! Me llamo {self.nombre}
        Soy de color {self.color}
        Tengo {self.edad} años
        """
        )


# ==============================
# EJEMPLOS DE USO
# ==============================

print("\n1. Creando nuestro primer gato:")
# Creamos un objeto (gato) usando nuestra clase como molde
gato1 = Gatos("Puna", "negro", 2)
gato1.presentarse()

print("\n2. Comportamientos del primer gato:")
gato1.comer()
gato1.dormir()
gato1.hacer_necesidades()

print("\n3. Creando un segundo gato:")
# Podemos crear tantos gatos como queramos
gato2 = Gatos("Roma", "blanco", 3)
gato2.presentarse()

print("\n4. Comportamientos del segundo gato:")
gato2.comer()
gato2.dormir()
gato2.hacer_necesidades()

# ==============================
# EJEMPLO AVANZADO
# ==============================

print("\n5. Creando una lista de gatos:")
# Podemos crear múltiples gatos y guardarlos en una lista
gatos = [
    Gatos("Puna", "marron", 1),
    Gatos("Roma", "blanca y negra", 4),
    Gatos("Milo", "manchado", 2),
]

print("\n6. Haciendo que todos los gatos se presenten:")
# Esto también es un for, solo que usado de otra forma!
for gato in gatos:
    gato.presentarse()
