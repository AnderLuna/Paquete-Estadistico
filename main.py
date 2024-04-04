import math  # Importa el módulo math para operaciones matemáticas avanzadas
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para trazar gráficos

# Función para recibir los datos de entrada del usuario
def recibir_datos():
    valores = []  # Inicializa una lista vacía para almacenar los valores ingresados
    continuar = True  # Bandera para controlar el bucle de entrada de datos
    while continuar:
        entrada = input("Ingrese los datos separados por coma o 'fin' para terminar: ")  # Solicita al usuario que ingrese los datos
        if entrada.lower() == 'fin':  # Verifica si el usuario desea finalizar la entrada de datos
            continuar = False  # Cambia la bandera para salir del bucle
        else:
            valores.extend(entrada.split(','))  # Divide la entrada por comas y agrega los valores a la lista
    return valores  # Devuelve la lista de valores ingresados

# Función para validar si todos los elementos de una lista son números
def validar_numeros(valores):
    return all(valor.replace('.', '').isdigit() for valor in valores)  # Retorna True si todos los valores son dígitos

# Función para ordenar los datos numéricos de manera ascendente
def ordenar_datos(valores):
    valores_sin_etiquetas = [valor for valor in valores if valor.replace('.', '').isdigit()]  # Filtra los valores no numéricos
    return sorted(map(float, valores_sin_etiquetas))  # Convierte los valores a números flotantes y los ordena

# Función para que el usuario seleccione el tipo de tabla de frecuencia
def seleccionar_tipo_tabla():
    opcion = input("¿Qué tipo de tabla de frecuencia prefiere? (simple/intervalos): ").lower()  # Solicita al usuario que seleccione el tipo de tabla
    if opcion == 'simple' or opcion == 'intervalos':  # Verifica si la opción ingresada es válida
        return opcion  # Devuelve la opción seleccionada por el usuario
    else:
        print("Opción inválida. Por favor, ingrese 'simple' o 'intervalos'.")  # Informa al usuario que la opción ingresada es inválida
        return seleccionar_tipo_tabla()  # Llama recursivamente a la función para que el usuario ingrese una opción válida

# Función para calcular el número óptimo de intervalos (regla de Sturges)
def calcular_numero_intervalos(valores):
    num_total_valores = len(valores)  # Calcula el número total de valores
    num_intervalos = math.sqrt(num_total_valores)  # Calcula el número de intervalos
    num_intervalos = round(num_intervalos)  # Redondea el número de intervalos
    if num_intervalos % 2 == 0:  # Si el número de intervalos es par, se incrementa en 1 para evitar problemas de agrupación
        num_intervalos += 1
    return int(num_intervalos)  # Devuelve el número de intervalos como un entero

# Función para calcular el rango de los datos
def calcular_rango(valores):
    min_valor = min(valores)  # Obtiene el valor mínimo de la lista
    max_valor = max(valores)  # Obtiene el valor máximo de la lista
    rango = max_valor - min_valor  # Calcula el rango restando el valor máximo al valor mínimo
    return rango  # Devuelve el rango de los datos

# Función para calcular la amplitud de los intervalos
def calcular_amplitud(num_intervalos, rango):
    amplitud = rango / num_intervalos  # Calcula la amplitud dividiendo el rango entre el número de intervalos
    if amplitud % 1 != 0:  # Si la amplitud no es un número entero
        amplitud = round(amplitud)  # Redondea la amplitud al entero más cercano
    return int(amplitud)  # Devuelve la amplitud como un entero

# Función para calcular los intervalos
def calcular_intervalos(valores, amplitud, num_intervalos):
    valor_minimo = min(valores)  # Obtiene el valor mínimo de la lista
    valor_maximo = max(valores)  # Obtiene el valor máximo de la lista
    
    intervalos = []  # Inicializa una lista vacía para almacenar los intervalos
    for i in range(num_intervalos):
        inicio = valor_minimo + (amplitud * i)  # Calcula el límite inferior del intervalo
        fin = inicio + amplitud  # Calcula el límite superior del intervalo
        intervalos.append((inicio, fin))  # Agrega el intervalo a la lista de intervalos
    
    return {'Intervalos': intervalos}  # Devuelve los intervalos como un diccionario

# Función para calcular las marcas de clase de los intervalos
def calcular_marca_clase(intervalos):
    marcas_clase = []  # Inicializa una lista vacía para almacenar las marcas de clase
    for inicio, fin in intervalos['Intervalos']:
        marca_clase = (inicio + fin) / 2  # Calcula la marca de clase como el punto medio del intervalo
        marcas_clase.append(marca_clase)  # Agrega la marca de clase a la lista de marcas de clase
    return {'Marcas de Clase': marcas_clase}  # Devuelve las marcas de clase como un diccionario

# Función para calcular las frecuencias de los datos
def calcular_frecuencias(valores, intervalos=None):
    frecuencias = {}  # Inicializa un diccionario vacío para almacenar las frecuencias
    if intervalos:  # Si se proporcionan intervalos
        for inicio, fin in intervalos['Intervalos']:
            # Cuenta el número de valores que caen dentro de cada intervalo y lo asigna como frecuencia
            frecuencias[(inicio, fin)] = sum(1 for valor in valores if inicio <= valor < fin)
    else:  # Si no se proporcionan intervalos
        for valor in valores:
            if valor in frecuencias:
                frecuencias[valor] += 1  # Incrementa la frecuencia si el valor ya está en el diccionario
            else:
                frecuencias[valor] = 1  # Agrega el valor al diccionario con una frecuencia inicial de 1
    return frecuencias  # Devuelve las frecuencias como un diccionario

# Función para calcular las frecuencias acumuladas de los datos
def calcular_frecuencias_acumuladas(frecuencias):
    acumulado = 0  # Inicializa una variable para almacenar la suma acumulada de frecuencias
    frec_acumuladas = {}  # Inicializa un diccionario vacío para almacenar las frecuencias acumuladas
    for valor, frecuencia in frecuencias.items():
        acumulado += frecuencia  # Agrega la frecuencia actual al acumulado
        frec_acumuladas[valor] = acumulado  # Asigna la frecuencia acumulada al valor correspondiente
    return frec_acumuladas  # Devuelve las frecuencias acumuladas como un diccionario

# Función para calcular las frecuencias relativas de los datos
def calcular_frecuencias_relativas(frecuencias, total_valores):
    frec_relativas = {}  # Inicializa un diccionario vacío para almacenar las frecuencias relativas
    for valor, frecuencia in frecuencias.items():
        frec_relativas[valor] = frecuencia / total_valores  # Calcula la frecuencia relativa y la asigna al valor correspondiente
    return frec_relativas  # Devuelve las frecuencias relativas como un diccionario

# Función para calcular las frecuencias relativas acumuladas de los datos
def calcular_frecuencias_relativas_acumuladas(frec_relativas):
    acumulado = 0  # Inicializa una variable para almacenar la suma acumulada de frecuencias relativas
    frec_relativas_acumuladas = {}  # Inicializa un diccionario vacío para almacenar las frecuencias relativas acumuladas
    for valor, frec_relativa in frec_relativas.items():
        acumulado += frec_relativa  # Agrega la frecuencia relativa actual al acumulado
        frec_relativas_acumuladas[valor] = acumulado  # Asigna la frecuencia relativa acumulada al valor correspondiente
    return frec_relativas_acumuladas  # Devuelve las frecuencias relativas acumuladas como un diccionario

# Función para calcular las frecuencias relativas porcentuales de los datos
def calcular_frecuencias_relativas_porcentuales(frec_relativas):
    frec_porcentuales = {}  # Inicializa un diccionario vacío para almacenar las frecuencias relativas porcentuales
    for valor, frec_relativa in frec_relativas.items():
        frec_porcentuales[valor] = frec_relativa * 100  # Calcula la frecuencia relativa porcentual y la asigna al valor correspondiente
    return frec_porcentuales  # Devuelve las frecuencias relativas porcentuales como un diccionario

# Función para calcular las frecuencias acumuladas porcentuales de los datos
def calcular_frecuencias_acumuladas_porcentuales(frec_acumuladas, total_valores):
    frec_acum_porcentuales = {}  # Inicializa un diccionario vacío para almacenar las frecuencias acumuladas porcentuales
    for valor, frec_acumulada in frec_acumuladas.items():
        frec_acum_porcentuales[valor] = (frec_acumulada / total_valores) * 100  # Calcula la frecuencia acumulada porcentual y la asigna al valor correspondiente
    return frec_acum_porcentuales  # Devuelve las frecuencias acumuladas porcentuales como un diccionario

# Función para mostrar la tabla de frecuencia simple
def mostrar_tabla_simple(valores, frecuencias, total_valores):
    print("Tabla de Frecuencia Simple:")  # Imprime el encabezado de la tabla
    print("--------------------------------------------------")  # Imprime la línea divisoria superior
    print("| Valor | Frecuencia | Frecuencia Acumulada | Frecuencia Relativa | Frecuencia Relativa Acumulada | Frecuencia Relativa Porcentual | Frecuencia Acumulada Porcentual |")  # Imprime las etiquetas de las columnas
    print("--------------------------------------------------")  # Imprime la línea divisoria inferior
    frec_acumulada = 0  # Inicializa una variable para almacenar la frecuencia acumulada
    frec_relativa_acumulada = 0  # Inicializa una variable para almacenar la frecuencia relativa acumulada
    for valor, frec_absoluta in frecuencias.items():  # Itera sobre los valores y sus frecuencias
        frec_relativa = frec_absoluta / total_valores  # Calcula la frecuencia relativa
        frec_acumulada += frec_absoluta  # Actualiza la frecuencia acumulada
        frec_relativa_acumulada += frec_relativa  # Actualiza la frecuencia relativa acumulada
        frec_porcentual = frec_relativa * 100  # Calcula la frecuencia relativa porcentual
        frec_acum_porcentual = frec_acumulada / total_valores * 100  # Calcula la frecuencia acumulada porcentual
        # Imprime una fila de la tabla con los valores calculados
        print(f"| {valor} | {frec_absoluta} | {frec_acumulada} | {frec_relativa:.2f} | {frec_relativa_acumulada:.2f} | {frec_porcentual:.2f}% | {frec_acum_porcentual:.2f}% |")
    print("--------------------------------------------------")  # Imprime la línea divisoria inferior

# Función para mostrar la tabla de frecuencia por intervalos
def mostrar_tabla_intervalos(intervalos, marca_clase, frecuencias, total_valores):
    print("Tabla de Frecuencia por Intervalos:")  # Imprime el encabezado de la tabla
    print("----------------------------------------------------------------------------------------------------------------------------")  # Imprime la línea divisoria superior
    print("| Intervalo   | Marca de Clase | F. Absoluta | F. Absoluta Acumulada | F. Relativa | F. Relativa Acumulada | F. Relativa Porcentual | F. Acumulada Porcentual |")  # Imprime las etiquetas de las columnas
    print("----------------------------------------------------------------------------------------------------------------------------")  # Imprime la línea divisoria inferior
    frec_acumulada = 0  # Inicializa una variable para almacenar la frecuencia acumulada
    frec_relativa_acumulada = 0  # Inicializa una variable para almacenar la frecuencia relativa acumulada
    for i, (inicio, fin) in enumerate(intervalos['Intervalos']):  # Itera sobre los intervalos y sus frecuencias
        frec_absoluta = frecuencias[(inicio, fin)]  # Obtiene la frecuencia absoluta del intervalo
        marca = marca_clase['Marcas de Clase'][i]  # Obtiene la marca de clase del intervalo
        frec_relativa = frec_absoluta / total_valores  # Calcula la frecuencia relativa del intervalo
        frec_acumulada += frec_absoluta  # Actualiza la frecuencia acumulada
        frec_relativa_acumulada += frec_relativa  # Actualiza la frecuencia relativa acumulada
        frec_porcentual = frec_relativa * 100  # Calcula la frecuencia relativa porcentual del intervalo
        frec_acum_porcentual = frec_acumulada / total_valores * 100  # Calcula la frecuencia acumulada porcentual del intervalo
        # Imprime una fila de la tabla con los valores calculados
        print(f"| [{inicio:.2f}, {fin:.2f}) | {marca:.2f} | {frec_absoluta} | {frec_acumulada} | {frec_relativa:.2f} | {frec_relativa_acumulada:.2f} | {frec_porcentual:.2f}% | {frec_acum_porcentual:.2f}% |")
    print("----------------------------------------------------------------------------------------------------------------------------")  # Imprime la línea divisoria inferior

# Función para calcular la media de los datos
def calcular_media(valores):
    return sum(valores) / len(valores)  # Calcula la media como la suma de los valores dividida por el número de valores

# Función para calcular la mediana de los datos
def calcular_mediana(valores):
    n = len(valores)  # Obtiene la longitud de la lista de valores
    sorted_vals = sorted(valores)  # Ordena los valores de manera ascendente
    if n % 2 == 0:  # Si hay un número par de valores
        return (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2  # Calcula la mediana como el promedio de los dos valores centrales
    else:  # Si hay un número impar de valores
        return sorted_vals[n // 2]  # La mediana es el valor central

# Función para calcular la moda de los datos
def calcular_moda(valores):
    frecuencias = {}  # Inicializa un diccionario vacío para almacenar las frecuencias de los valores
    for valor in valores:
        if valor in frecuencias:
            frecuencias[valor] += 1  # Incrementa la frecuencia si el valor ya está en el diccionario
        else:
            frecuencias[valor] = 1  # Agrega el valor al diccionario con una frecuencia inicial de 1
    moda_frecuencia = max(frecuencias.values(), default=0)  # Obtiene la frecuencia más alta de los valores
    if moda_frecuencia == 1:  # Si todas las frecuencias son 1, no hay moda
        return "No hay moda"
    modas = [valor for valor, frecuencia in frecuencias.items() if frecuencia == moda_frecuencia]  # Obtiene los valores con la frecuencia más alta
    return modas  # Devuelve los valores que más se repiten

# Función para crear y mostrar un histograma de los datos
def crear_histograma(intervalos, frecuencias):
    bins = [f"{inicio:.2f}-{fin:.2f}" for inicio, fin in intervalos['Intervalos']]  # Crea los nombres de los intervalos
    valores = [frecuencias[(inicio, fin)] for inicio, fin in intervalos['Intervalos']]  # Obtiene las frecuencias de los intervalos
    
    plt.figure(figsize=(10, 6))  # Crea una nueva figura para el gráfico
    plt.bar(bins, valores, color='blue', edgecolor='black')  # Crea un gráfico de barras con los intervalos y sus frecuencias
    plt.xlabel('Intervalos')  # Etiqueta del eje x
    plt.ylabel('Frecuencia')  # Etiqueta del eje y
    plt.title('Histograma')  # Título del gráfico
    plt.xticks(rotation=45, ha='right')  # Rota las etiquetas del eje x para una mejor visualización
    plt.show()  # Muestra el gráfico

# Bloque principal del programa
if __name__ == "__main__":
    valores = recibir_datos()  # Llama a la función para recibir los datos del usuario
    if not validar_numeros(valores):  # Verifica si los datos ingresados son numéricos
        print("Error: Se ingresaron valores no numéricos.")  # Imprime un mensaje de error si se ingresan valores no numéricos
    else:
        valores_ordenados = ordenar_datos(valores)  # Ordena los valores numéricos
        tipo_tabla = seleccionar_tipo_tabla()  # Llama a la función para que el usuario seleccione el tipo de tabla
        num_intervalos = calcular_numero_intervalos(valores_ordenados)  # Calcula el número óptimo de intervalos
        rango = calcular_rango(valores_ordenados)  # Calcula el rango de los datos
        amplitud = calcular_amplitud(num_intervalos, rango)  # Calcula la amplitud de los intervalos
        intervalos = calcular_intervalos(valores_ordenados, amplitud, num_intervalos)  # Calcula los intervalos
        marca_clase = calcular_marca_clase(intervalos)  # Calcula las marcas de clase de los intervalos
        frecuencias_intervalos = calcular_frecuencias(valores_ordenados, intervalos)  # Calcula las frecuencias de los intervalos
        frecuencias_simple = calcular_frecuencias(valores_ordenados)  # Calcula las frecuencias simples
        total_valores = len(valores_ordenados)  # Obtiene el número total de valores

        if tipo_tabla == 'simple':  # Si se selecciona una tabla simple
            mostrar_tabla_simple(valores_ordenados, frecuencias_simple, total_valores)  # Muestra la tabla de frecuencia simple
        else:  # Si se selecciona una tabla de intervalos
            mostrar_tabla_intervalos(intervalos, marca_clase, frecuencias_intervalos, total_valores)  # Muestra la tabla de frecuencia por intervalos

        # Calcula y muestra la media, mediana y moda
        media = calcular_media(valores_ordenados)  # Calcula la media
        mediana = calcular_mediana(valores_ordenados)  # Calcula la mediana
        moda = calcular_moda(valores_ordenados)  # Calcula la moda
        print(f"Media: {media}")  # Imprime la media
        print(f"Mediana: {mediana}")  # Imprime la mediana
        print(f"Moda: {moda}")  # Imprime la moda
        crear_histograma(intervalos, frecuencias_intervalos)  # Crea y muestra un histograma de los datos