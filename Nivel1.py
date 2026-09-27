#EJERCICIO 1
def crear_formato(prefijo, fn_transformacion):
    def formatear(texto):
        texto_transformado = fn_transformacion(texto)
        return f"{prefijo}{texto_transformado}"
    return formatear

mayusculas = crear_formato(">>", lambda texto: texto.upper())
print(mayusculas("Hola Kenneth"))

invertir = crear_formato("<<", lambda texto: texto[::-1])
print(invertir("Hola Kenneth"))

#EJERCICIO2

def crear_operador(factor, operacio_lambda):
    def operar(numero):
        return operacio_lambda(numero, factor)
    return operar

sumar_10 = crear_operador(10, lambda a, b: a + b)
print(sumar_10(5))

multiplicar_por_3 = crear_operador(3, lambda a, b: a * b)
print(multiplicar_por_3(7))

potenciar_a_2 = crear_operador(2, lambda a, b: a ** b)
print(potenciar_a_2(4))

# EJERCICIO 3

def crear_descuento_dinamico(regla_condicional_lambda, porcentaje= 0.10):
    def calcular(precio):
        if regla_condicional_lambda(precio):
            descuento = precio * porcentaje
            return precio - descuento
        return precio
    return calcular

descuento_mayor_100 = crear_descuento_dinamico(lambda precio: precio > 100, 0.20)
print(descuento_mayor_100(200))  
print(descuento_mayor_100(120))

descuento_par = crear_descuento_dinamico(lambda precio: precio % 2 == 0, 0.15)
print(descuento_par(100))
print(descuento_par(50))

# EJERCICIO 4

def crear_generador_surtijos(patron_lambda):
    contador = 0
    def generar_(nombre_base):
        nonlocal contador
        contador += 1
        sufijo = patron_lambda(contador)
        return f"{nombre_base}{sufijo}"
    return generar_

generador_serial = crear_generador_surtijos(lambda n: f"_{n:03d}")
print(generador_serial("reporte"))
print(generador_serial("reporte"))
print(generador_serial("foto"))

generador_version = crear_generador_surtijos(lambda n: f"_v{n}")
print(generador_version("app"))
print(generador_version("app"))

# EJERCICIO 5

def crear_conversor(tasa, margen_lamba):
    def convertir(monto):
        comision = margen_lamba(monto)
        total = (monto * tasa) + comision
        return  round(total, 2)
    return convertir

usd_a_eur = crear_conversor(0.92, lambda m: m * 0.02)
print(usd_a_eur(100))

usd_a_cop = crear_conversor(4000, lambda m: 5000)
print(usd_a_cop(100))

usd_a_mxn = crear_conversor(18.5, lambda m: m * 0.03 if m > 50 else 0)
print(usd_a_mxn(100))
print(usd_a_mxn(30))
print(usd_a_mxn(50))

