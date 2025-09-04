def pedir_nombre():
    return input("¿Cuál es tu nombre? ").strip()

def pedir_edad():
    while True:
        try:
            edad = int(input("¿Cuántos años tienes? "))
            if edad > 0:
                return edad
            print("La edad debe ser un número positivo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def pedir_altura():
    while True:
        try:
            altura = float(input("¿Cuánto mides (en metros)? "))
            if 0.5 < altura < 2.5:
                return altura
            print("Ingresa una altura razonable (entre 0.5 y 2.5 metros).")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def pedir_programador():
    while True:
        respuesta = input("¿Eres programador (sí/no)? ").strip().lower()
        if respuesta in ["sí", "no"]:
            return respuesta == "sí"
        print("Responde solo con 'sí' o 'no'.")

def prog(es_programador):
    return "es programador" if es_programador else "no es programador"

# 🧠 Flujo principal
nombre = pedir_nombre()
edad = pedir_edad()
altura = pedir_altura()
es_programador = pedir_programador()

print(f"{nombre} tiene {edad} años, mide {altura} metros, y {prog(es_programador)}.")
