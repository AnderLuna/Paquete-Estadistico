import math

def recibir_datos():
    valores = []
    continuar = True
    while continuar:
        entrada = input("Ingrese los datos separados por coma o 'fin' para terminar: ")
        if entrada.lower() == 'fin':
            continuar = False
        else:
            valores.extend(entrada.split(','))
    return valores

def validar_numeros(valores):
    return all(valor.replace('.', '').isdigit() for valor in valores)

def ordenar_datos(valores):
    valores_sin_etiquetas = [valor for valor in valores if valor.replace('.', '').isdigit()]
    return sorted(map(float, valores_sin_etiquetas))

def recomendar_tabla_frecuencia(valores):
    if len(set(valores)) <= 12:
        return "simple"
    else:
        return "intervalos"

def seleccionar_tipo_tabla():
    opcion = input("¿Qué tipo de tabla de frecuencia prefiere? (simple/intervalos): ").lower()
    if opcion == 'simple' or opcion == 'intervalos':
        return opcion
    else:
        print("Opción inválida. Por favor, ingrese 'simple' o 'intervalos'.")
        return seleccionar_tipo_tabla()

import math

def calcular_numero_intervalos(valores):
    num_total_valores = len(valores)
    num_intervalos = math.sqrt(num_total_valores)
    num_intervalos = round(num_intervalos)
    if num_intervalos % 2 == 0:  # Si el número de intervalos es par, sumar 1
        num_intervalos += 1
    
    return int(num_intervalos)

def calcular_rango(valores):
    min_valor = min(valores)
    max_valor = max(valores)
    rango = max_valor - min_valor
    return rango

def calcular_amplitud(num_intervalos, rango):
    amplitud = rango / num_intervalos
    
    if amplitud % 1 != 0:
        amplitud = round(amplitud)
    
    return int(amplitud)

def calcular_intervalos(valores, amplitud, num_intervalos):
    valor_minimo = min(valores)
    valor_maximo = max(valores)
    
    intervalos = []
    for i in range(num_intervalos):
        inicio = valor_minimo + (amplitud * i)
        fin = inicio + amplitud
        intervalos.append((inicio, fin))
    
    return {'Intervalos': intervalos}

def calcular_marca_clase(intervalos):
    marcas_clase = []
    for inicio, fin in intervalos['Intervalos']:
        marca_clase = (inicio + fin) / 2
        marcas_clase.append(marca_clase)
    return {'Marcas de Clase': marcas_clase}

def calcular_frecuencias(valores, intervalos=None):
    frecuencias = {}
    if intervalos:
        for inicio, fin in intervalos['Intervalos']:
            frecuencias[(inicio, fin)] = sum(1 for valor in valores if inicio <= valor < fin)
    else:
        for valor in valores:
            if valor in frecuencias:
                frecuencias[valor] += 1
            else:
                frecuencias[valor] = 1
    return frecuencias

def calcular_frecuencias_acumuladas(frecuencias):
    acumulado = 0
    frec_acumuladas = {}
    for valor, frecuencia in frecuencias.items():
        acumulado += frecuencia
        frec_acumuladas[valor] = acumulado
    return frec_acumuladas

def calcular_frecuencias_relativas(frecuencias, total_valores):
    frec_relativas = {}
    for valor, frecuencia in frecuencias.items():
        frec_relativas[valor] = frecuencia / total_valores
    return frec_relativas

def calcular_frecuencias_relativas_acumuladas(frec_relativas):
    acumulado = 0
    frec_relativas_acumuladas = {}
    for valor, frec_relativa in frec_relativas.items():
        acumulado += frec_relativa
        frec_relativas_acumuladas[valor] = acumulado
    return frec_relativas_acumuladas

def calcular_frecuencias_relativas_porcentuales(frec_relativas):
    frec_porcentuales = {}
    for valor, frec_relativa in frec_relativas.items():
        frec_porcentuales[valor] = frec_relativa * 100
    return frec_porcentuales

def calcular_frecuencias_acumuladas_porcentuales(frec_acumuladas, total_valores):
    frec_acum_porcentuales = {}
    for valor, frec_acumulada in frec_acumuladas.items():
        frec_acum_porcentuales[valor] = (frec_acumulada / total_valores) * 100
    return frec_acum_porcentuales

def mostrar_tabla_simple(valores, frecuencias, total_valores):
    print("Tabla de Frecuencia Simple:")
    print("--------------------------------------------------")
    print("| Valor | Frecuencia | Frecuencia Acumulada | Frecuencia Relativa | Frecuencia Relativa Acumulada | Frecuencia Relativa Porcentual | Frecuencia Acumulada Porcentual |")
    print("--------------------------------------------------")
    frec_acumulada = 0
    frec_relativa_acumulada = 0
    for valor, frec_absoluta in frecuencias.items():
        frec_relativa = frec_absoluta / total_valores
        frec_acumulada += frec_absoluta
        frec_relativa_acumulada += frec_relativa
        frec_porcentual = frec_relativa * 100
        frec_acum_porcentual = frec_acumulada / total_valores * 100
        print(f"| {valor} | {frec_absoluta} | {frec_acumulada} | {frec_relativa:.2f} | {frec_relativa_acumulada:.2f} | {frec_porcentual:.2f}% | {frec_acum_porcentual:.2f}% |")
    print("--------------------------------------------------")

def mostrar_tabla_intervalos(intervalos, marca_clase, frecuencias, total_valores):
    print("Tabla de Frecuencia por Intervalos:")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("| Intervalo   | Marca de Clase | F. Absoluta | F. Absoluta Acumulada | F. Relativa | F. Relativa Acumulada | F. Relativa Porcentual | F. Acumulada Porcentual |")
    print("----------------------------------------------------------------------------------------------------------------------------")
    frec_acumulada = 0
    frec_relativa_acumulada = 0
    for i, (inicio, fin) in enumerate(intervalos['Intervalos']):
        frec_absoluta = frecuencias[(inicio, fin)]
        marca = marca_clase['Marcas de Clase'][i]
        frec_relativa = frec_absoluta / total_valores
        frec_acumulada += frec_absoluta
        frec_relativa_acumulada += frec_relativa
        frec_porcentual = frec_relativa * 100
        frec_acum_porcentual = frec_acumulada / total_valores * 100
        print(f"| [{inicio:.2f}, {fin:.2f}) | {marca:.2f} | {frec_absoluta} | {frec_acumulada} | {frec_relativa:.2f} | {frec_relativa_acumulada:.2f} | {frec_porcentual:.2f}% | {frec_acum_porcentual:.2f}% |")
    print("----------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    valores = recibir_datos()
    if not validar_numeros(valores):
        print("Error: Se ingresaron valores no numéricos.")
    else:
        valores_ordenados = ordenar_datos(valores)
        tipo_tabla = seleccionar_tipo_tabla()

        if tipo_tabla == 'simple':
            frecuencias = calcular_frecuencias(valores_ordenados)
            total_valores = len(valores_ordenados)
            mostrar_tabla_simple(valores_ordenados, frecuencias, total_valores)
        else:
            num_intervalos = calcular_numero_intervalos(valores_ordenados)
            rango = calcular_rango(valores_ordenados)
            amplitud = calcular_amplitud(num_intervalos, rango)
            intervalos = calcular_intervalos(valores_ordenados, amplitud, num_intervalos)
            marca_clase = calcular_marca_clase(intervalos)
            frecuencias = calcular_frecuencias(valores_ordenados, intervalos)
            total_valores = len(valores_ordenados)
            mostrar_tabla_intervalos(intervalos, marca_clase, frecuencias, total_valores)