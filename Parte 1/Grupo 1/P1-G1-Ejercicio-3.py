# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

### 3. Secuencia de Fibonacci: Genera los primeros N números de la secuencia de Fibonacci, donde N es un número proporcionado por el usuario.

# Pedir al usuario cuántos números de Fibonacci quiere
numero = int(input("¿Cuántos números de Fibonacci quieres?"))

# Iniciar los 2 primeros números de Fibonacci
a, b = 0, 1

# Crear lista para guardar secuencia
fibonacci = []

# Calcular los primeros N números de la secuencia de Fibonacci, donde cada número es la suma de los dos anteriores
for _ in range(numero):
    fibonacci.append(a)
    a, b = b, a + b

# Mostrar los primeros N números de la secuencia de Fibonacci
print(f"Los primeros {numero} números de la secuencia de Fibonacci son", fibonacci)