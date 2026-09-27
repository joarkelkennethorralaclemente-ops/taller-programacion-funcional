# EJERCICIO 6

def crear_contador_paso(fn_paso):
    cuenta = 0
    def contar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return contar

print("=== NIVEL 2 - EJERCICIO 6 ===")
c1 = crear_contador_paso(lambda c: c+5)
print(c1())
print(c1())
print(c1())

c2 = crear_contador_paso(lambda c: c*2+1)
print(c2())
print(c2())
print(c2())

# EJERCICIO 7

def crear_acumulador_validor(criterio_lambda):
    total=0
    def agregar(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return agregar

print("\n== NIVEL 2 - EJERCICIO 7 ===")
acum_positivos = crear_acumulador_validor(lambda v: v > 0)
print(acum_positivos(55))
print(acum_positivos(-5))
print(acum_positivos(20))
print(acum_positivos(-1))

acum_pares = crear_acumulador_validor(lambda v: v%2 == 0)
print(acum_pares(3))
print(acum_pares(4))
print(acum_pares(7))
print(acum_pares(6))

# EJERCICIO 8

def crear_promediador_filtrador(filtro_ruido_lambda):
    datos = []
    def agregar(valor):
        nonlocal datos
        if not filtro_ruido_lambda(valor):
            datos.append(valor)
        if not datos:
            return 0
        return round(sum(datos) / len(datos),2)
    return agregar

print ("\n=== NIVEL 2 - EJERCICIO 8 ===")
prom = crear_promediador_filtrador(lambda v: v>100)
print(prom (10))
print(prom (20))
print(prom (500))
print(prom (30))
print(prom (200))

#EJERCICIO 9

def crear_limitador_avanzado(max_intentos, fn_alerta):
    contador = 0

    def ejecutador():
        nonlocal contador
        contador += 1
        if contador > max_intentos:
            fn_alerta(contador)
            return False
        return True

    return ejecutador

print("\n=== NIVEL 2 - EJERCICIO 9 ===")
limite = crear_limitador_avanzado(3, lambda n: print(f"Limite superado: intento #{n}"))
print(limite())  # True
print(limite())  # True
print(limite())  # True
print(limite())  # False

#EJERCICIO 10

def crear_conmutador(list_estado):
    indice = -1 
    def siguiente():
        nonlocal indice
        indice = (indice + 1)% len(list_estado)
        return list_estado[indice]
    return siguiente

print("\n=== NIVEL 2 - EJERCICIO 10 ===")
semaforo = crear_conmutador(["ROJO","AMARILLO","VERDE"])
print(semaforo())
print(semaforo())
print(semaforo())
print(semaforo())

