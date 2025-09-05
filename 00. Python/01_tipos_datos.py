# Tipos de datos en Python y conceptos claves

# Tipos de datos basicos
entero = int(10)          # Entero
flotante = float(10.5)    # Flotante
cadena = str("Hola")      # Cadena de texto
booleano = bool(True)     # Booleano
listas = list([1, 2, 3])  # Lista
dictado = dict(a=1, b=2)  # Diccionario
tupla = tuple((1, 2, 3))  # Tupla
conjunto = set([1, 2, 3]) # Conjunto

# Operadores: Aritmeticos(+, -, *, /), logicos (and, or, not), de comparacion (==, !=, >, <)
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3

## Logicos
Y = suma and resta
o = suma or resta
NO = not suma    

## Comparacion
igual = (suma == resta)
diferente = (suma != resta)
mayor = (suma > resta)
menor = (suma < resta)

## Condicionales
# IF - ELSE - ELIF
if suma > resta:
    resultado = "Suma es mayor"
elif suma < resta:
    resultado = "Resta es mayor"
else:
    resultado = "Son iguales"
    
## Bucles
# FOR
for i in range(5):
    print(i)
# WHILE
contador = 0
while contador < 5:
    print(contador)
    contador += 1

## Funciones
def saludar(nombre):
    return f"Hola, {nombre}"

def parametros(nombre="Mundo"):
    return f"Hola, {nombre}"

def retorno(objeto):
    return print(objeto)

## MAnejo de errores
try:
    resultado = 10 / 0
except ZeroDivisionError:
    resultado = "Error: Division por cero"
finally:
    print("Ejecucion finalizada")
    
## Modularidad
import math as m
raiz_cuadrada = m.sqrt(16)