# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

### 2. Verificador de Números Primos: Escribe un programa que solicite un número al usuario e indique si es un número primo o no.

# Pedir un número al usuario
numero = int(input("Ingresa un número: "))

# Definir variable de numero primo como verdadera
es_primo = True

# Verificar si el número tiene divisores distintos de 1 y él mismo

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0: # Si se divide exactamente por i
            es_primo = False
            break #no seguir revisando

# Indicar si el número es primo o no
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")