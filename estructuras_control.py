# ==============================
# Estructuras de Control en Python
# ==============================

# ==============================
# 1. if, elif, else
# ==============================

# Ejemplo básico de if
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejemplo con if, elif y else
numero = 5
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejemplo con múltiples condiciones
temperatura = 25
if temperatura < 10:
    print("Hace mucho frío")
elif temperatura < 20:
    print("Está fresco")
elif temperatura < 30:
    print("Temperatura agradable")
else:
    print("Hace calor")


# ==============================
# 2. match-case (Python 3.10+)
# ==============================

# Ejemplo básico de match-case (equivalente a switch en otros lenguajes)
dia = "lunes"
match dia.lower():
    case "lunes":
        print("Es el primer día de la semana")
    case "martes":
        print("Es el segundo día de la semana")
    case "miércoles":
        print("Es el tercer día de la semana")
    case "jueves":
        print("Es el cuarto día de la semana")
    case "viernes":
        print("¡Por fin es viernes!")
    case "sábado" | "domingo":  # Ejemplo de múltiples casos
        print("¡Es fin de semana!")
    case _:  # Caso por defecto
        print("Día no válido")


# El mismo ejemplo anterior pero usando if-elif-else
dia = "lunes"
dia = dia.lower()  # Convertimos a minúsculas para hacer la comparación case-insensitive

if dia == "lunes":
    print("Es el primer día de la semana")
elif dia == "martes":
    print("Es el segundo día de la semana")
elif dia == "miércoles":
    print("Es el tercer día de la semana")
elif dia == "jueves":
    print("Es el cuarto día de la semana")
elif dia == "viernes":
    print("¡Por fin es viernes!")
elif dia == "sábado" or dia == "domingo":
    print("¡Es fin de semana!")
else:
    print("Día no válido")
