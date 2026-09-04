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
# =========== EJERCICIO NUMERO 11 ===========
# Pedimos al usuario que introduzca su edad
try:
    edad = int(input("Introduce tu edad: "))

    # Comprobamos si la edad está dentro del rango
    if edad < 0 or edad > 120:
        # Lanzamos un ValueError manualmente porque el valor es incorrecto
        raise ValueError

    print(f"Tu edad es: {edad}")

# Si el usuario pone algo que no es un número o un número fuera del rango
except ValueError:
    print("Error: Debes introducir un número válido entre 0 y 120.")

# Cualquier otro error
except:
    print("Error no especificado.")

# Final de proceso
finally:
    print("Operación finalizada")

"""
Había otra manera sin tener que lanzar la excepción manualmente pero es menos eficiente:
try:
    # Pedimos la edad al usuario e intentamos convertirla a entero
    edad = int(input("Introduce tu edad: "))

    # Comprobamos si la edad está dentro del rango permitido
    # Si está fuera del rango, no lanza una excepción automáticamente,
    # así que simplemente mostramos un mensaje
    if edad < 0 or edad > 120:
        print("Error: La edad debe estar entre 0 y 120.")
    else:
        print(f"Tu edad es: {edad}")

# Si el usuario introduce algo que no es un número
except ValueError:
    print("Error: Debes introducir un valor numérico.")

# Cualquier otro error inesperado
except:
    print("Ocurrió un error inesperado.")

# Este bloque se ejecuta siempre
finally:
    print("Finalizando el proceso...")

"""
# =========== EJERCICIO NUMERO 12 ===========
def longitudes_palabras(frase):
    # Dividimos la frase en palabras usando split() ya que por defecto separa los elementos por los espacios
    # Esto genera una lista como ["hola", "mundo"]
    palabras = frase.split()

    # Usamos map() para ver la longitud de cada palabra de la lista
    # map() devuelve un objeto iterable, así que lo convertimos en lista
    largura = list(map(len, palabras))

    # Devolvemos la lista con la largura de cada palabra
    return largura

print(longitudes_palabras("Hoy me apetece programar en python"))

# =========== EJERCICIO NUMERO 13 ===========
def mayus_minus(caracteres):
    # Convertimos todo a minúsculas para evitar duplicados (set es case sensitive)
    caracteres_normalizados = [c.lower() for c in caracteres]

    # Eliminamos duplicados con set()
    caracteres_unicos = set(caracteres_normalizados)

    # Creamos las tuplas (mayúscula, minúscula) usando map()
    resultado = list(map(lambda letra: (letra.upper(), letra.lower()), caracteres_unicos))

    return resultado


print(mayus_minus(["a", "b", "A", "c", "C", "d"]))

# =========== EJERCICIO NUMERO 14 ===========
def palabras_por_letra(lista_palabras, letra):
    # Usamos filter() para quedarnos solo con las palabras que empiezan por la letra entrada por parámetros
    resultado = list(filter(lambda palabra: palabra.lower().startswith(letra), lista_palabras))

    return resultado

palabras = ["gato", "perro", "gallina", "casa", "Girasol", "pato"]
print(palabras_por_letra(palabras, "g"))

# =========== EJERCICIO NUMERO 15 ===========
def suma_tres(lista_numeros):
    return list(map(lambda x: x + 3, lista_numeros))

numeros = [1, 5, 10]
print(suma_tres(numeros))

# =========== EJERCICIO NUMERO 16 ===========
def palabras_largas(frase, n):
    # Convertimos la frase en una lista de palabras, split por defecto separa por espacios
    palabras = frase.split()

    # Usamos filter() para quedarnos solo con las palabras que su longitud sea más grande que n
    resultado = list(filter(lambda palabra: len(palabra) > n, palabras))

    return resultado

texto = "Los desarrolladores crean aplicaciones increíbles"
print(palabras_largas(texto, 5))

# =========== EJERCICIO NUMERO 17 ===========
from functools import reduce

def lista_a_numero(digitos):
    # Usamos reduce() para ir construyendo el número paso a paso.
    # 'acumulado' guarda el número que llevamos formado.
    # 'd' es el siguiente dígito de la lista.
    # En cada paso multiplicamos el acumulado por 10 y sumamos el dígito.
    # Ejemplo: [5,7,2] → (((5*10)+7)*10)+2 → 572
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)

print(lista_a_numero([5, 7, 2]))

# =========== EJERCICIO NUMERO 18 ===========
# Creamos la lista de diccionarios desde cero
estudiantes = []

# Añadimos estudiantes manualmente
estudiantes.append({"nombre": "Ana", "edad": 20, "calificacion": 95})
estudiantes.append({"nombre": "Luis", "edad": 22, "calificacion": 88})
estudiantes.append({"nombre": "María", "edad": 19, "calificacion": 90})
estudiantes.append({"nombre": "Carlos", "edad": 21, "calificacion": 76})
estudiantes.append({"nombre": "Sofía", "edad": 23, "calificacion": 99})

# Usamos filter() para obtener solo los estudiantes con calificación >= 90
estudiantes_destacados = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))

# Mostramos el resultado
print(estudiantes_destacados)

# =========== EJERCICIO NUMERO 19 ===========
def filtrar_impares(lista_numeros):
    return list(filter(lambda x: x % 2 != 0, lista_numeros))
# La función mira si dividiendo cada número de la lista por dos, el resïduo de la
# división es 0 o no. Si no lo es, es impar y añade el número a la lista de impares

numeros = [1, 5, 10, 20, 7, 2, 6, 8]
print(filtrar_impares(numeros))

# =========== EJERCICIO NUMERO 20 ===========
def solo_enteros(lista):
    # filter() recorre la lista y se queda solo con los elementos
    # cuyo tipo sea exactamente int
    return list(filter(lambda elemento_lista: type(elemento_lista) is int, lista))

datos = [3, "hola", 7, "23", 10, "python", 5]
print(solo_enteros(datos))

# =========== EJERCICIO NUMERO 21 ===========
cubo = lambda n: n ** 3 # Crea una función pequeña y sencilla como es multiplicar el número dado por 3 para conseguir el cubo

print(cubo(4))  # Ejemplos de uso
print(cubo(2))  
# =========== EJERCICIO NUMERO 22 ===========
from functools import reduce

def producto_total(lista):
    # reduce() va acumulando el resultado.
    # En cada paso multiplica el acumulado por el siguiente número.
    # Ejemplo: [2, 3, 4] → (((2*3)*4)) = 24
    return reduce(lambda acumulado, num: acumulado * num, lista)

numeros = [2, 3, 4, 5]
print(producto_total(numeros))

# =========== EJERCICIO NUMERO 23 ===========
from functools import reduce

def concatenar_palabras(lista_palabras):
    # En cada paso junta la palabra con la siguiente.
    return reduce(lambda acumulado, palabra: acumulado + palabra, lista_palabras)

palabras = ["Hola", "Mundo", "!"]
print(concatenar_palabras(palabras))

# =========== EJERCICIO NUMERO 24 ===========
from functools import reduce

def diferencia_total(lista):
    # reduce() va restando cada número al acumulado.
    return reduce(lambda acumulado, x: acumulado - x, lista)

numeros = [20, 5, 3, 2]
print(diferencia_total(numeros))

# =========== EJERCICIO NUMERO 25 ===========
def contar_caracteres(cadena):
    # len() devuelve la cantidad total de caracteres en la cadena
    return len(cadena)

texto = "Hoy no he ido al mercado"
print(contar_caracteres(texto))

# =========== EJERCICIO NUMERO 26 ===========
resto = lambda a, b: a % b # Se crea la función lambda corta y sencilla para poder ejecutarla en una sola línea 

print(resto(10, 4)) # Ejemplos
print(resto(20, 4))
print(resto(7, 2))

# =========== EJERCICIO NUMERO 27 ===========
def promedio(lista):
    # Sumamos todos los valores y dividimos entre la cantidad de elementos
    return sum(lista) / len(lista)

numeros = [4, 8, 6, 10]
print(promedio(numeros))

# =========== EJERCICIO NUMERO 28 ===========
def primer_duplicado(lista):
    vistos = set()  # Conjunto inicializado para guardar los elementos ya encontrados

    for elemento in lista:
        if elemento in vistos:   # Si ya lo hemos visto, es el primer duplicado
            return elemento
        vistos.add(elemento)     # Si no, lo añadimos al conjunto

    return None  # Si no hay duplicados, devolvemos None

numeros = [3, 5, 2, 8, 5, 10, 2]
print(primer_duplicado(numeros))

# =========== EJERCICIO NUMERO 29 ===========
def enmascarar(variable):
    cadena = str(variable)  # Convertimos la variable a texto
    resultado = ""          # Aquí construiremos la cadena enmascarada

    # Recorremos la cadena con un índice
    for i in range(len(cadena)):
        # Si estamos en los últimos 4 caracteres, los dejamos tal cual
        if i >= len(cadena) - 4:
            resultado += cadena[i]
        else:
            resultado += "#"  # Enmascaramos el resto

    return resultado

print(enmascarar("123456789"))
print(enmascarar(987654321))
print(enmascarar("hola"))

# =========== EJERCICIO NUMERO 30 ===========
def son_anagramas(palabra1, palabra2):
    # Convertimos ambas palabras a minúsculas para evitar diferencias por mayúsculas
    p1 = palabra1.lower()
    p2 = palabra2.lower()

    # Ordenamos las letras de cada palabra y comparamos
    return sorted(p1) == sorted(p2)


# Imprimimos el resultado por pantalla
print(son_anagramas("Sergio", "Riesgos")) 
print(son_anagramas("Delira", "Lidera"))   
print(son_anagramas("Hola", "Halo"))

# =========== EJERCICIO NUMERO 30 ===========
def buscar_nombre():
    try:
        # Pedimos al usuario que ingrese nombres separados por comas
        entrada = input("Ingresa una lista de nombres separados por comas: ")

        # Convertimos la cadena en una lista de nombres
        lista_nombres = [nombre.strip() for nombre in entrada.split(",")]

        # Pedimos el nombre que queremos buscar
        nombre_buscar = input("Ingresa el nombre que quieres buscar: ").strip()

        # Si el nombre está en la lista, lo mostramos
        if nombre_buscar in lista_nombres:
            print("Nombre encontrado:", nombre_buscar)
        else:
            # Lanzamos una excepción si no está
            raise Exception("El nombre no se encuentra en la lista.")

    # Capturamos cualquier excepción que ocurra
    except Exception as error:
        print("Error:", error)

buscar_nombre()
