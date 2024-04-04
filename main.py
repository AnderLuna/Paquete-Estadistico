import math

def recibir_datos():
   categoria = input("Ingrese la categoría: ")
   datos = {categoria: []}
   continuar = True
   while continuar:
       entrada = input("Ingrese los datos separados por coma o 'fin' para terminar: ")
       if entrada.lower() == 'fin':
           continuar = False
       else:
           valores = entrada.split(',')
           if validar_numeros(valores):
               datos[categoria].extend(map(float, valores))
           else:
               print("Error: Los datos ingresados deben ser numéricos. Inténtelo de nuevo.")
   return datos

def validar_numeros(valores):
   return all(valor.replace('.', '').isdigit() for valor in valores)

def ordenar_datos(valores):
   return sorted(valores)

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

def calcular_numero_intervalos(valores):
    num_total_valores = len(valores)
    num_intervalos = 1 + 3.322 * math.log(num_total_valores)
    
    # Redondear al entero impar más cercano si el resultado es decimal
    if num_intervalos % 1 != 0:
        num_intervalos = round(num_intervalos)
        if num_intervalos % 2 == 0:  # Si el entero redondeado es par, ajustar al siguiente impar
            num_intervalos += 1
    
    return num_intervalos

def calcular_rango(valores):
    min_valor = min(valores)
    max_valor = max(valores)
    rango = max_valor - min_valor
    return rango

def calcular_amplitud(num_intervalos, rango):
    amplitud = rango / num_intervalos
    
    # Redondear al entero siguiente si la amplitud es decimal
    if amplitud % 1 != 0:
        amplitud = round(amplitud)
    
    return amplitud

def calcular_intervalos(valores, amplitud, num_intervalos):
    valor_minimo = valores[0]  # Obtenemos el valor mínimo
    valor_maximo = valores[-1]  # Obtenemos el valor máximo
    
    # Calculamos el tamaño de cada intervalo
    tamano_intervalo = amplitud
    
    # Creamos los intervalos
    intervalos = []
    valor_inicio = valor_minimo
    for _ in range(num_intervalos):
        valor_fin = valor_inicio + amplitud
        intervalos.append([valor_inicio, valor_fin])
        valor_inicio = valor_fin
    
    return {'Intervalos': intervalos}
    
def calcular_marca_clase(intervalos):
    marcas_clase = []
    for intervalo in intervalos:
        marca_clase = (intervalo[0] + intervalo[1]) / 2
        marcas_clase.append(marca_clase)
    return {'Marcas de Clase': marcas_clase}
    
def calcular_frecuencias(valores):
   frecuencias = {}
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


def tabla_frecuencia_simple(valores, frecuencias, total_valores):
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

def tabla_frecuencia_intervalos(intervalos, marca_clase, frecuencias, total_valores):
    print("Tabla de Frecuencia por Intervalos:")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("| Intervalo   | Marca de Clase | F. Absoluta | F. Absoluta Acumulada | F. Relativa | F. Relativa Acumulada | F. Relativa Porcentual | F. Acumulada Porcentual |")
    print("----------------------------------------------------------------------------------------------------------------------------")
    frec_acumulada = 0
    frec_relativa_acumulada = 0
    for i, (inicio, fin) in enumerate(intervalos):
        frec_absoluta = frecuencias[i]
        marca = marca_clase[i]
        frec_relativa = frec_absoluta / total_valores
        frec_acumulada += frec_absoluta
        frec_relativa_acumulada += frec_relativa
        frec_porcentual = frec_relativa * 100
        frec_acum_porcentual = frec_acumulada / total_valores * 100
        print(f"| [{inicio:.2f}, {fin:.2f}) | {marca:.2f} | {frec_absoluta} | {frec_acumulada} | {frec_relativa:.2f} | {frec_relativa_acumulada:.2f} | {frec_porcentual:.2f}% | {frec_acum_porcentual:.2f}% |")
    print("----------------------------------------------------------------------------------------------------------------------------")

datos = recibir_datos()
valores_ordenados = ordenar_datos(datos)
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
    frecuencias = calcular_frecuencias(valores_ordenados)
    total_valores = len(valores_ordenados)
    mostrar_tabla_intervalos(intervalos, marca_clase, frecuencias, total_valores)