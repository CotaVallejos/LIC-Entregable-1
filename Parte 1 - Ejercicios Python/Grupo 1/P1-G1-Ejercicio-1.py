# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

### 1. Calculadora de Factorial: Crea una función que reciba un número entero y devuelva su factorial.

# Pedir un número al usuario
numero = int(input("Ingresa un número: "))

# Inicializar factorial en 1
factorial = 1

# Multiplicar todos los números desde 1 hasta numero
for i in range(1, numero + 1):
    factorial *= i
    
# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}.")