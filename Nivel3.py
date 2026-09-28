#EJERCICIO 11

def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    filtrados = filter(fn_predicado, lista)
    return list(map(fn_transformacion, filtrados))

print("\n=== NIVEL 3- EJERCICIO 11 ===")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = procesar_coleccion(
    numeros,
    lambda x: x%2 ==0,
    lambda x: x**2
)
print(resultado)

#EJERCICIO 12

def agrupar_por(lista, fn_clave):
    grupos = {}
    for item in lista:
        clave = fn_clave(item)
        grupos.setdefault(clave, []).append(item)
    return grupos

print("\n=== EJERCIICO 12: Agrupador Personalizando ===")
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Quito"},
    {"nombre": "Luis", "edad": 30, "ciudad": "Guayaquil"},
    {"nombre": "Sofia", "edad": 35, "ciudad": "Guayaquil"},
    {"nombre": "Pedro", "edad": 40, "ciudad": "Quito"},
]
por_edad = agrupar_por(personas, lambda p: p["edad"])
for edad, grupo in por_edad.items():
    print(f"Edad {edad}: {[p['nombre'] for p in grupo]}")
    
por_ciudad = agrupar_por(personas, lambda p: p["ciudad"])
for ciudad, grupo in por_ciudad.items():
    print(f"ciudad {ciudad}: {[p['nombre'] for p in grupo]}")

#EJERCICIO 13

def ejecutar_y_rastrear(fn_tarea, n):
    historial = []
    def ejecutar(*args):
        for _ in range(n):
            resultado = fn_tarea(*args)
            historial.append(resultado)
        return historial
    return ejecutar

print("\n=== NIVEL 3 - EJERCICIO 13 ===")
ejecutar =ejecutar_y_rastrear(lambda x: x*2,3)
print(ejecutar(6))
print(ejecutar(10))

# EJERcicio 14

def componer_dos(f,g):
    def compuesta(x):
        return f(g(x))
    return compuesta

print("\n=== NIVEL 3 - EJERCICIO 14 ===")
sumar_1 = lambda x:x+1
duplicar = lambda x:x*2
combinada = componer_dos(sumar_1, duplicar)
print(combinada(5))

mayusculas = lambda s: s.upper()
exclamar = lambda s: s+"!"
gritar = componer_dos(exclamar, mayusculas)
print(gritar("hola que tal, como vas"))

#EJERCICIO 15
import time

def auditar_ejecutar(fn_objetivo, fn_logger):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = fn_objetivo(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        fn_logger({
            "funcion": fn_objetivo.__name__,
            "duracion": round(duracion, 6),
            "resultado": resultado
        })
        return resultado
    return wrapper

print("\n=== NIVEL 3 - EJERCICIO 15 ===")

def sumar_lento(a, b):
    time.sleep(0.01)
    return a + b

logger = lambda info: print(info)
sumar_lento = auditar_ejecutar(sumar_lento, logger)
print(sumar_lento(3, 4))
