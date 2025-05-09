# ==============================
# 1. Bucle While
# ==============================

# Ejemplo básico de while con break
print("Ejemplo de while con break:")
while True:
    print("hola")
    break  # Rompe el bucle infinito después de una iteración

# Ejemplo de while con contador
print("\nEjemplo de while con contador:")
contador = 1  # Inicializamos el contador
while contador <= 5:  # Condición: mientras el contador sea menor o igual a 5
    print(f"El contador va por el número: {contador}")
    contador += 1  # Incrementamos el contador en cada iteración


# ==============================
# 2. Bucle For
# ==============================

# El bucle for se usa cuando conocemos el rango o la colección a iterar
print("\nEjemplo de for con range:")
for i in range(1, 6):  # Itera desde 1 hasta 5 (6 no incluido)
    print(f"El contador va por el número: {i}")

# Ejemplo de for con una lista
print("\nEjemplo de for con lista:")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Fruta actual: {fruta}")

# ==============================
# 3. Control de Bucles
# ==============================

print("\nEjemplo de break y continue:")
for numero in range(1, 6):
    if numero == 2:
        continue  # Salta a la siguiente iteración
    if numero == 4:
        break  # Rompe el bucle completamente
    print(f"Número actual: {numero}")
