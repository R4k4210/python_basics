# ==============================
# FUNCIONES EN PYTHON
# ==============================

# ==============================
# 1. Funciones sin parámetros
# ==============================


def ejemplo():
    """
    Función simple que imprime números del 1 al 5
    """
    print("\nEjemplo de función sin parámetros:")
    for i in range(1, 6):
        print(f"El contador va por el número: {i}")


# Llamada a la función
ejemplo()


# ==============================
# 2. Funciones con parámetros
# ==============================


def saludar(nombre):
    """
    Función que saluda a una persona
    Args:
        nombre (str): Nombre de la persona a saludar
    """
    print(f"\nHola, ¿cómo estás {nombre}?")


# Ejemplos de llamadas con diferentes argumentos
print("\nEjemplos de función con parámetros:")
saludar("Dolo")
saludar("Santi")
saludar("Dani")


# ==============================
# 3. Funciones con retorno
# ==============================


def sumar(num1, num2, num3):
    """
    Función que suma tres números
    Args:
        num1 (int): Primer número
        num2 (int): Segundo número
        num3 (int): Tercer número
    Returns:
        int: La suma de los tres números
    """
    return num1 + num2 + num3


print("\nEjemplos de función con retorno:")

# Ejemplo 1: Invocación simple
print("Suma simple:", sumar(5, 5, 10))

# Ejemplo 2: Guardando el resultado en una variable
resultado = sumar(2, 3, 4)
print("Resultado guardado en variable:", resultado)

# Ejemplo 3: Usando el resultado en una operación
resultado2 = 10 + sumar(2, 3, 4)
print("Resultado en operación:", resultado2)


# ==============================
# 4. Funciones con valores por defecto
# ==============================


def multiplicar(a, b=2):
    """
    Función que multiplica dos números, con valor por defecto
    Args:
        a (int): Primer número
        b (int, optional): Segundo número. Por defecto es 2
    Returns:
        int: El producto de los dos números
    """
    return a * b


print("\nEjemplos de función con valores por defecto:")
print("Multiplicar 5 * 2 (valor por defecto):", multiplicar(5))
print("Multiplicar 5 * 3 (valor especificado):", multiplicar(5, 3))
