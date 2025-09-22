# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

### 6. Contador de Vocales y Consonantes: Pide al usuario que ingrese una frase y cuenta cuántas vocales y consonantes contiene.

# Pedir al usuario que ingrese una frase
frase_usuario = input("Ingresa una frase: ")

# Definir vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"

# Crear contadores
contador_vocales = 0
contador_consonantes = 0

# Recorrer cada letra de la frase
for letra in frase_usuario:
    if letra.isalpha(): # sólo cuenta letras, no números, espacios, etc
        if letra in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1


# Mostrar cuántas vocales y consonantes contiene la frase
print(f"La frase tiene {contador_vocales} vocales y {contador_consonantes} consonantes.")
