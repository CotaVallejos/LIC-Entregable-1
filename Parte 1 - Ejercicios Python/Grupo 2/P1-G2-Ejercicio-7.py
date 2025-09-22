# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

### 7. Verificador de Palíndromos: Crea una función que determine si una palabra o frase ingresada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda, ignorando espacios y mayúsculas).

def es_palindromo(texto):
    # 1. Convertir todo a minúsculas
    texto = texto.lower()
    # 2. Quitar espacios
    texto = texto.replace(" ", "")
    # 3. Comparar con el texto al revés
    return texto == texto[::-1]

# Pedir al usuario que ingrese una palabra o frase
frase_usuario = input("Ingresa una palabra o frase: ")

# Verificar si es palíndromo
if es_palindromo(frase_usuario):
    print("¡Yay, es un palíndromo! :)")
else:
    print("Lo siento, no es un palíndromo :(")
