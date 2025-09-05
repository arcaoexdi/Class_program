# Tipos de datos en Python y conceptos claves

# Tipos de datos basicos

# Entero
entero = int(11)
print("Este es un dato entero ", entero)

# Flotante
flotante = float(105)    
print("Este es un dato flotante ",flotante)

# Cadena de texto
cadena = str("Por ende es un String")
print("Este es un dato tipo cadena, ",cadena)

# Booleano
booleano = bool(False)     
print("Este es un dato tipo booleano, por ende, es verdadero o: ",booleano)

# Lista
listas = list([1, 2, 3])  
print("Este es un dato tipo lista ",listas)

# Diccionario
dictado = dict(a=1, b=2)  
print("Este es un dato tipo dictado, el cual da como resultado la siguiente expresion ",dictado)

# Tupla
tupla = tuple(('simpres', "dobles", "numero en comillas: 3", flotante, entero))  
print("Este es un dato tipo tupla ", tupla)

# Conjunto
conjunto = set([1, entero, "Hola mundo"]) 
print("Este es un dato tipo conjunto ",conjunto)


# Operadores: Aritmeticos(+, -, *, /), logicos (and, or, not), de comparacion (==, !=, >, <)
suma = 5 + 3
print("Este es el resultado de la suma ",suma)

resta = 5 - 7
print("Este es el resultado de la resta ",resta)

multiplicacion = 5 * 3
print("Este es el resultado de la multiplicacion ",multiplicacion)

division = 5 / 3
print("Este es el resultado de la division ",division)  

## Logicos
Y = suma and resta
print("Este es el resultado del operador AND ",Y)

o = suma or resta
print("Este es el resultado del operador OR ",o)

NO = not resta
print("Este es el resultado del operador NOT ",NO)

## Comparacion
igual = (suma == resta)
print("Este es el resultado del operador de comparacion igual ",igual)

diferente = (suma != resta)
print("Este es el resultado del operador de comparacion diferente ",diferente)

mayor = (suma > resta)
print("Este es el resultado del operador de comparacion mayor ",mayor)

menor = (suma < resta)
print("Este es el resultado del operador de comparacion menor ",menor)

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
    print("Iteracion sobre el numero 5: ",i)

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