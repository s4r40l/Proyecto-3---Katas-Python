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
def buscar_palabras(lista_palabras, objetivo):
    resultado = []  # Lista donde guardaremos las palabras que contienen el objetivo

    for palabra in lista_palabras:  # Recorremos cada palabra de la lista original
        if objetivo in palabra:  # Comprobamos si la palabra objetivo aparece dentro de la palabra actual
            resultado.append(palabra)  # Si la contiene, la añadimos a la lista resultado

    return resultado  # Devolvemos la lista final con todas las coincidencias

palabras = ["ordenador", "coche", "ordenar", "composición", "correr","comer"] # Lista de palabras
print(buscar_palabras(palabras, "ordena")) # Imprimir por pantalla el resultado de la función con la lista de palabras y el objetivo como parámetros

# =========== EJERCICIO NUMERO 4 ===========
def diferencias(listaA, listaB):
    # Usamos map() para aplicar una operación a cada par de elementos de ambas listas.
    # La función lambda recibe dos valores (x de lista1 y y de lista2)
    # y devuelve la diferencia entre ellos.
    resultado = list(map(lambda x, y: x - y, listaA, listaB))

    return resultado  # Devolvemos la lista con todas las diferencias calculadas

a = [10, 20, 30]
b = [1, 5, 7]

print(diferencias(a, b)) # Imprimir por pantalla el resultado de la función con los dos arrays como parámetros

# =========== EJERCICIO NUMERO 5 ===========
def evaluar_media(numeros, nota_aprobado=5): # Parámetros de la función, la segunda es opcional y si no viene con valor, el predeterminado es el 5
    # Calculamos la media sumando todos los valores y dividiéndolos entre la cantidad de elementos
    media = sum(numeros) / len(numeros)

    # Comprobamos si la media es mayor o igual que la nota mínima para aprobar
    if media >= nota_aprobado:
        estado = "aprobado"   # Si cumple, el estado es aprobado
    else:
        estado = "suspenso"   # Si no cumple, el estado es suspenso

    # Devolvemos una tupla con la media y el estado
    return (media, estado)

print(evaluar_media([4, 6, 8, 5]))

# =========== EJERCICIO NUMERO 6 ===========
def factorial(num):
    # Cuando num es 0 o 1, el factorial es 1
    if num == 0 or num == 1:
        return 1

    # Llamamos a la función otra vez con n-1
    # y multiplicamos ese resultado por n
    return num * factorial(num - 1)

print(factorial(5))

# =========== EJERCICIO NUMERO 7 ===========
datos = [(1, 2), ("hola", "mundo"), ("DAM", 2026)]

def tuplas_a_strings(lista_tuplas):
    # Creamos una transformación usando map().
    # map() aplica una función a cada elemento de la lista.
    # En este caso, cada elemento es una tupla como (1, 2) o ("hola", "mundo").

    # La función lambda recibe una tupla 'tup'.
    # Queremos convertir esa tupla en un string.
    # Para ello, recorremos cada elemento de la tupla y lo convertimos a texto con str(x).
    # Luego usamos " ".join(...) para unir todos los elementos en un solo string separados por espacios.
    # Ejemplo: (1, 2) → "1 2"
    # Ejemplo: ("hola", "mundo") → "hola mundo"

    resultado = list(
        map(
            lambda tup: " ".join(
                str(x) for x in tup  # Convertimos cada elemento de la tupla a string
            ),
            lista_tuplas  # Esta es la lista original de tuplas
        )
    )

    # Convertimos el resultado de map() en una lista normal usando list().
    # Finalmente devolvemos esa lista de strings.
    return resultado

print(tuplas_a_strings(datos))

# =========== EJERCICIO NUMERO 8 ===========
try:
    # Pedimos los dos números al usuario
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    # Intentamos realizar la división
    resultado = num1 / num2

# Si el usuario pone algo que no es un número saltará ValueError
except ValueError:
    print("Error: Introduce valores numéricos válidos.")

# Si intenta dividir entre cero saltará ZeroDivisionError
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

# Si no ocurre ningún error, este bloque se ejecuta
else:
    print(f"Resultado: {resultado}")

# Este bloque se ejecuta siempre, ocurra o no ocurra un error
finally:
    print("Función finalizada.")

# =========== EJERCICIO NUMERO 9 ===========
def filtrar_mascotas(lista_mascotas):
    # Lista de mascotas prohibidas en España
    listaProhibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

    # Usamos filter() para quedarnos solo con las mascotas que NO están en la lista prohibida.
    # La función lambda recibe cada mascota y devuelve True si NO está prohibida.
    # filter() mantiene solo los elementos donde la condición es True.
    mascotas_filtradas = list(filter(lambda mascota: mascota not in listaProhibidas, lista_mascotas))

    # Devolvemos la nueva lista
    return mascotas_filtradas

mascotas = ["Perro", "Gato", "Mapache", "Tortuga", "Oso", "Canario"]
print(filtrar_mascotas(mascotas))

# =========== EJERCICIO NUMERO 10 ===========
def calcular_promedio(numeros):
    try:
        # Intentamos calcular el promedio
        # Si la lista está vacía, esto provocará un ZeroDivisionError
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio es: {promedio}")

    # Si la lista está vacía len(numeros) es 0 y no se puede dividir entre cero
    except ZeroDivisionError:
        print("Error: La lista está vacía, no se puede chacer el cálculo")

    # Si la lista contiene elementos no numéricos sum() fallará
    except TypeError:
        print("Error: No se pueden sumar los elementos de la lista")

    # Cualquier otro error
    except:
        print("Error")

    # Este bloque se ejecuta siempre
    finally:
        print("Operación finalizada")

calcular_promedio([4, 6, 8])
calcular_promedio([])
calcular_promedio([4, "hola", 8])
# =========== EJERCICIO NUMERO 11 ===========

# =========== EJERCICIO NUMERO 12 ===========
