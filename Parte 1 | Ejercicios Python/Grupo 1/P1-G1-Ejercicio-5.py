# Parte 1: 20 Ejercicios Intermedios de Python

## Grupo 1: Fundamentos y Lógica (Ejercicios 1-5)

### 5. Conversor de Temperatura: Crea dos funciones, una para convertir de grados Celsius a Fahrenheit y otra para hacer la conversión inversa.

temperature = int(input("Temperature: "))

unit = input("Is it (C)elsius or (F)ahrenheit?: ")

if unit.upper() == "C":
    converted = (temperature * 1.8) + 32
    print("Temperature in Fahrenheit: " + str(converted))
else:
    converted = (temperature - 32) / 1.8
    print("Temperature in Celsius: " + str(converted))
