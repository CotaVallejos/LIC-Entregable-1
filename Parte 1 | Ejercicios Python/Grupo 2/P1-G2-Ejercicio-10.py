# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 2: Manipulación de Cadenas y Listas (Ejercicios 6-10)

### 10. Ordenamiento de Lista (Burbuja): Implementa el algoritmo de ordenamiento de burbuja para ordenar una lista de números de menor a mayor sin usar la función sort().

# Definir la función que reciba una lista de números
def bubble_sort(lista):
    n = len(lista) # Conocer cuántas comparaciones habrá que hacer
    # Recorrer todos los elementos
    for i in range(n):
        # Últimos i elementos ya están en orden, no hace falta revisarlos
        for j in range(n -i - 1):
            # Comparar elemento actual con el siguiente
            if lista[j] > lista[j + 1]:
                # Intercambiar si están en orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    # Devolver la lista ordenada al final
    return lista

# Crear una lista de números desordenados
lista = [9, 5, 7, 2, 8, 4, 3, 10, 1, 6]

# Pasar lista a la función
lista_ordenada = bubble_sort(lista)

# Mostrar lista ordenada
print("Lista ordenada de menor a mayor: ", lista_ordenada)
