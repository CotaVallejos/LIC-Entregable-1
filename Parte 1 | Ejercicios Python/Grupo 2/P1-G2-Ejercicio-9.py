# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

### 9. Buscador de Elementos Comunes: Escribe una función que reciba dos listas y devuelva una nueva lista con los elementos que ambas tienen en común.

# Crear dos listas
lista_1 = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = [1, 3, 5, 7, 9]

# Crear una lista nueva para guardar los elementos que ambas tienen en común
lista_unica = []

# Recorrer primera lista
for elemento in lista_1:
    if elemento in lista_2: # Recorrer segunda lista
        if elemento not in lista_unica: # Evitar duplicados
            lista_unica.append(elemento)

# Mostrar elementos que ambas listas tienen en común
print(lista_unica)



