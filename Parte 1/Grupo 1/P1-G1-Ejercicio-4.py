# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

### 4. Adivina el Número: El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo y el programa le dará pistas ("más alto" o "más bajo").

import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Inicializar la variable del usuario
numero_usuario = -1

# Mientras el usuario no adivine
while numero_usuario != numero_secreto:
# Pedir al usuario que adivine el número
    numero_usuario = int(input("¡Adivina el número! Ingresa un número entre 1 y 100:"))

    if numero_usuario == numero_secreto:
        print(f"¡Felicitaciones, adivinaste! El número es {numero_secreto}.")
    elif numero_usuario > numero_secreto:
        print("Más bajo")
    else:
        print("Más alto")