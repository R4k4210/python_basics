# ==============================
# GUÍA DE GIT Y GITHUB PARA PRINCIPIANTES
# ==============================

"""
¿Qué es Git?
------------
Git es un sistema de control de versiones que nos permite:
- Guardar el historial de cambios de nuestro código
- Trabajar en equipo sin pisarnos el código
- Volver a versiones anteriores si algo sale mal
- Crear diferentes versiones (ramas) de nuestro proyecto

¿Qué es GitHub?
--------------
GitHub es una plataforma web que:
- Almacena repositorios Git en la nube
- Permite colaborar con otros desarrolladores
- Ofrece herramientas como Issues, Pull Requests, Actions
- Funciona como portfolio para programadores

Comandos Básicos de Git:
-----------------------
1. Configuración inicial:
   git config --global user.name "Tu Nombre"
   git config --global user.email "tu@email.com"

2. Iniciar un repositorio nuevo:
   git init

3. Ver estado del repositorio:
   git status  # Muestra archivos modificados, nuevos, eliminados

4. Guardar cambios:
   git add archivo.py    # Añade un archivo específico
   git add .            # Añade todos los archivos
   git commit -m "Descripción del cambio"

5. Trabajar con GitHub:
   git remote add origin https://github.com/usuario/repositorio.git
   git push -u origin main  # Sube cambios a GitHub
   git pull                # Descarga cambios de GitHub

6. Trabajar con ramas:
   git branch              # Ver ramas
   git branch nombre-rama  # Crear rama
   git checkout rama       # Cambiar a una rama
   git merge rama         # Unir rama con la actual

Flujo de trabajo básico:
------------------------
1. Crear/modificar archivos
2. git add . (preparar cambios)
3. git commit -m "mensaje" (guardar cambios)
4. git push (subir a GitHub)

Cómo iniciar un proyecto desde cero:
-----------------------------------
1. Crear repositorio en GitHub:
   - Ir a github.com
   - Click en '+' -> 'New repository'
   - Dar nombre y descripción
   - Crear repositorio

2. Iniciar repositorio local:
   git init
   git add .
   git commit -m "Primer commit"

3. Conectar con GitHub:
   git remote add origin https://github.com/usuario/repositorio.git
   git branch -M main  # Cambiar rama master a main
   git push -u origin main

Cambiar de master a main:
------------------------
# Si estás en una rama master y quieres cambiarla a main:
git branch -M main

Comandos útiles adicionales:
---------------------------
git log                 # Ver historial de commits
git diff               # Ver cambios en archivos
git restore archivo    # Deshacer cambios en archivo
git reset --hard HEAD  # Volver al último commit
git clone URL          # Clonar repositorio existente

Buenas prácticas:
----------------
1. Hacer commits frecuentes y pequeños
2. Escribir mensajes de commit descriptivos
3. Crear ramas para nuevas funcionalidades
4. Hacer pull antes de push
5. No subir contraseñas ni archivos sensibles

Archivos importantes:
--------------------
.gitignore  # Lista de archivos que Git debe ignorar
README.md   # Documentación principal del proyecto

Para ignorar archivos:
---------------------
# Crear archivo .gitignore y añadir:
__pycache__/
*.pyc
.env
.vscode/
"""

# Ejemplo de uso básico:
print(
    """
# 1. Iniciar repositorio
git init

# 2. Crear/modificar archivos
touch archivo.py

# 3. Verificar estado
git status

# 4. Preparar cambios
git add archivo.py

# 5. Guardar cambios
git commit -m "Añadido archivo.py"

# 6. Subir a GitHub
git push
"""
)
