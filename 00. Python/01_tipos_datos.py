# Tipos de datos en Python y conceptos claves

# Tipos de datos basicos

# Entero
entero = input("Ingresa un numero entero sin punto: ")
entero = int(entero)
print("Este es un dato entero sin punto: ", entero)

# Flotante
flotante = input("Ingresa un numero flotante con punto, no con coma: ")
flotante = float(flotante)
print("Este es un dato flotante: ", flotante, "con punto decimal")

# Cadena de texto
cadena = input("Ingresa una cadena de texto: ")
cadena = str(cadena)
print("Este es un dato tipo cadena: ", cadena)

# Booleano
booleano = bool(False)
if booleano is True:
    print("El dato booleano es verdadero")
else:
    print("El dato booleano es falso")


# Lista
# Paso 1: Pedir al usuario datos separados por espacios
entrada = input("Ingresa varios datos separados por espacios: ")

# Paso 2: Convertir la entrada en una lista
listas = entrada.split()

# Paso 3: Mostrar la lista inicial
print("Este es un dato tipo lista:", listas)

# Paso 4: Permitir agregar más elementos
nuevo_dato = input(
    "¿Quieres agregar otro dato? Escribe uno o varios separados por espacios: "
)
listas += nuevo_dato.split()

# Paso 5: Mostrar la lista actualizada
print("Lista actualizada:", listas)


# Diccionario
a = "God morning"
b = "Good night"
c = "Good afternoon"
dictado = dict(a=a, b=b, c=c)
print(
    "Este es un dato tipo dictado, el cual da como resultado la siguiente expresion: ",
    dictado,
)


# Tupla
tupla = tuple(("simpres", "dobles", "numero en comillas: 3", flotante, entero))
print("Este es un dato tipo tupla entre parentesis", tupla)

# Conjunto
conjunto = set([1, entero, "Hola mundo"])
print("Este es un dato tipo conjunto donde esta encerrado en llaves ", conjunto)


# Operadores: Aritmeticos(+, -, *, /)
# logicos (and, or, not), de comparacion (==, !=, >, <)
suma = 5 + 3
print("Este es el resultado de la suma ", suma)

resta = 5 - 7
print("Este es el resultado de la resta ", resta)

multiplicacion = 5 * 3
print("Este es el resultado de la multiplicacion ", multiplicacion)

division = 5 / 3
print("Este es el resultado de la division ", division)

## Logicos
Y = suma and resta
print("Este es el resultado del operador AND ", Y)

o = suma or resta
print("Este es el resultado del operador OR ", o)

NO = not resta
print("Este es el resultado del operador NOT ", NO)

## Comparacion
igual = suma == resta
print("Este es el resultado del operador de comparacion igual ", igual)

diferente = suma != resta
print("Este es el resultado del operador de comparacion diferente ", diferente)

mayor = suma > resta
print("Este es el resultado del operador de comparacion mayor ", mayor)

menor = suma < resta
print("Este es el resultado del operador de comparacion menor ", menor)

## Condicionales
# IF - ELSE - ELIF
if suma > resta:
    resultado1 = "Suma es mayor"
    print("Si es mayor, imprime esto", resultado1)
elif suma < resta:
    resultado2 = "Resta es mayor"
    print("Si es menor, imprime esto", resultado2)
else:
    resultado3 = "Son iguales"
    print("Si son iguales, imprime esto", resultado3)

## Bucles
# FOR
for i in range(5):
    print("Iteracion sobre el numero 5: ", i)

# WHILE
contador = 0
while contador < 5:
    print("Iterar sobre un contador que da como resultado: ", contador)
    contador += 1
    if contador == 5:
        print("Contador ha llegado a 5, saliendo del bucle")
        break


## Funciones
def saludar(nombre):
    print("Saludando a:", nombre)
    return f"Hola, {nombre}"


### Uso de la funcion Saludar
saludo = saludar(input("Ingrese su nombre: "))
print(saludo)


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
import math as m  # noqa: E402

raiz_cuadrada = m.sqrt(16)
