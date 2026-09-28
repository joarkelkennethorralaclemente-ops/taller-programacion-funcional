# EJERCICIO 16

def crear_validador_multiple(*lambdas_criterios):
    """Valida que un objeto cumpla TODAS las reglas."""
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar

validar_usuario = crear_validador_multiple(
    lambda u: len(u.get("nombre", "")) >= 3,
    lambda u: u.get("edad", 0) >= 18,
    lambda u: "@" in u.get("email", "")
)
print(validar_usuario({"nombre": "Ana", "edad": 21, "email": "a@x.com"}))
print(validar_usuario({"nombre": "Joarkel",  "edad": 25, "email": "a@x.com"}))
print(validar_usuario({"nombre": "Angie", "edad": 15, "email": "a@x.com"}))

#EJERCICIO 17

def memoria_avanzada(fn_costosa, max_items):
    cache = {}
    orden = []

    def wrapper(*args):
        key = args

        if key in cache:
            return cache[key]

        resultado = fn_costosa(*args)

        if len(cache) >= max_items:
            viejo = orden.pop(0)
            del cache[viejo]

        cache[key] = resultado
        orden.append(key)
        return resultado

    return wrapper

print("\n=== EJERCICIO 17: MEMORIZACION CON LIMITE ===")

def lenta(x):
    print(f" (calculando {x}...)")
    return x**2

rapida = memoria_avanzada(lenta, 2)
print(rapida(2))
print(rapida(3))
print(rapida(2))
print(rapida(4))
print(rapida(2))

#EJERCICIO 18

def crear_pipeline(*funciones_transformacion):
    def ejecutar(dato):
        resultado = dato
        for fn in funciones_transformacion:
            resultado = fn(resultado)
        return resultado
    return ejecutar

print("\n=== EJERCICIO 18: Pipeline Secuencial ===")
pipeline = crear_pipeline(
    lambda x: x+10,
    lambda x: x*2,
    lambda x: x**2
)    
print(pipeline(5))

#EJERCICIO 19 

def crear_sistema_evento():
    suscriptores={}
    def gestionar(accion, evento=None, callback=None, datos=None):
        if accion == "on":
            suscriptores.setdefault(evento, []). append(callback)
            return f"Suscripto a '{evento}'"
        elif accion == "emit":
            if evento not in suscriptores:
                return f"Nadie escucha '{evento}"
            for cb in suscriptores[evento]:
                cb(datos)
            return f"Evento '{evento}' emitido a { len(suscriptores[evento])} oyentes"
    return gestionar

print("\n=== EJERCICIO 19: Sistema Pub/Sub ===")
sistema = crear_sistema_evento()
print(sistema("on", "login", lambda d: print(f"  [A] Bienvenido {d}")))
print(sistema("on", "login", lambda d: print(f"  [B] Registrando acceso de {d}")))
print(sistema("emit", "login", datos="Ana"))
print(sistema("emit", "logout", datos="Ana"))

#EJERCICIO 20

def crear_consultor(campo):
    def crear_filtro(condicion_lambda):
        def consultar(lista):
            return [item for item in lista if condicion_lambda(item.get(campo))]
        return consultar
    return crear_filtro

print("\n=== EJERCICIO 20: Motor de miniconsultas ===")
productos = [
    {"nombre": "Laptop",  "precio": 1200, "stock": 5},
    {"nombre": "Mouse",   "precio": 25,   "stock": 50},
    {"nombre": "Monitor", "precio": 300,  "stock": 0},
    {"nombre": "Teclado", "precio": 80,   "stock": 20},
    {"nombre": "UPS", "precio": 70,   "stock": 10},
    {"nombre": "Memorias RAM", "precio": 1280,   "stock": 0},
]

consultar_precio = crear_consultor("precio")
caros = consultar_precio(lambda p: p > 100)
print([p["nombre"] for p in caros(productos)])

consultar_stock = crear_consultor("stock")
disponibles = consultar_stock(lambda s: s > 0)
print([p["nombre"] for p in disponibles(productos)])
