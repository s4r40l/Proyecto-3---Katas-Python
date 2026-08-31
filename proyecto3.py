# =========== EJERCICIO NUMERO 1 ===========
def frecuencias_letras(cadena):  # Definimos la función y le damos un parámetro llamado 'cadena'
    cadena = cadena.replace(" ", "")    # Quitamos todos los espacios para que no cuenten como caracteres
    frecuencias = {}  # Creamos un diccionario vacío donde guardaremos cada letra y cuántas veces aparece

    for letra in cadena:  # Recorremos la cadena letra por letra
        if letra in frecuencias:  # Si la letra ya existe como clave en el diccionario...
            frecuencias[letra] += 1  # ...sumamos 1 a su contador
        else:  # Si la letra aún no está en el diccionario...
            frecuencias[letra] = 1  # ...la añadimos con un contador inicial de 1

    return frecuencias  # Devolvemos el diccionario completo con todas las frecuencias

print(frecuencias_letras("hola mundo"))  # Llamamos a la función y mostramos el resultado por pantalla

# =========== EJERCICIO NUMERO 2 ===========
numeros = [1, 2, 3, 4, 5]  # Lista original de números

# Usamos map() para aplicar una función a cada elemento de la lista.
# La función lambda recibe un número x y devuelve x * 2 (su doble).
dobles = list(map(lambda x: x * 2, numeros))  # Convertimos el resultado de map en una lista

print(dobles)  # Mostramos la nueva lista con los valores duplicados

# =========== EJERCICIO NUMERO 3 ===========

# =========== EJERCICIO NUMERO 4 ===========

# =========== EJERCICIO NUMERO 5 ===========

# =========== EJERCICIO NUMERO 6 ===========

# =========== EJERCICIO NUMERO 7 ===========

# =========== EJERCICIO NUMERO 8 ===========

# =========== EJERCICIO NUMERO 9 ===========

# =========== EJERCICIO NUMERO 10 ===========

# =========== EJERCICIO NUMERO 11 ===========

# =========== EJERCICIO NUMERO 12 ===========
