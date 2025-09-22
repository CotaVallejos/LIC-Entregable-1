# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

### 8. Eliminar Duplicados de una Lista: Dada una lista, crea una nueva lista que contenga solo los elementos únicos de la original, sin repetir ninguno.

# Crear una lista
lista_nombres = ["Ana", "Camila", "Pedro", "Ana", "Marcela", "Pedro", "Lucia", "Rodrigo"]

# Crear una lista vacía para guardar los únicos
lista_nombres_unicos = []

# Agregar elementos en la lista de nombres únicos
for elemento in lista_nombres:
    if elemento not in lista_nombres_unicos: #si el elemento no está ya en la lista de nombres únicos
        lista_nombres_unicos.append(elemento)


# Mostrar una nueva lista que contenga sólo los elementos únicos de la original
print(lista_nombres_unicos)
