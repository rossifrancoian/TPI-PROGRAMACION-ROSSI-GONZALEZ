import csv
import statistics
import os

RUTA_CSV = "paises.csv"

# FUNCIONES DE ARCHIVO CSV
def cargar_paises(ruta):
    """
    Función:
        Abrir el archivo CSV (paises.csv) y cargar los datos de los países como una lista de diccionarios.
        En el proceso, convierte los datos de población y superficie de string a int. 
        En caso de error muestra un mensaje personalizado y devuelve una lista (paises) vacía.
    Parámetros: 
        Recibe como parametro la ruta del archivo CSV.
    Retorno: 
        Si el archivo no existe o hay errores devuelve una lista vacía.
        Si todo sale bien devuelve una lista de diccionario con los datos de cada país.
    """
    paises = []
    try:
        with open(ruta, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre":     fila["nombre"].strip(),
                    "poblacion":  int(fila["poblacion"].strip()),
                    "superficie": int(fila["superficie"].strip()),
                    "continente": fila["continente"].strip()
                })
        print(f"\n Se cargaron {len(paises)} países desde '{ruta}'.")
    except FileNotFoundError:
        print(f"\n No se encontró '{ruta}'. Se iniciará con un dataset vacío.")
    except ValueError as e:
        print(f"\n Error de formato en el CSV: {e}")
    except Exception as e:
        print(f"\n Error inesperado al cargar el CSV: {e}")
    return paises


def guardar_paises(ruta, paises):
    """
    Función:
        Sobrescribe el contenido del archivo CSV con la lista de los países.
        Incluye automaticamente la fila de encabezados como primera línea.
        En caso de error muestra un mensaje personalizado.
    Parámetros: 
        Ruta del arhivo CSV donde se guardarán los datos.
        Lista de diccionarios con los datos de cada país.
    Retorno:
        None
    """
    try:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)
        print(f"\n Datos guardados correctamente en '{ruta}'.")
    except Exception as e:
        print(f"\n Error al guardar el archivo: {e}")

# FUNCIONES DE VALIDACIÓN
def pedir_entero(mensaje, minimo=1):
    """
    Función:
        Solicita al usuario que ingrese un número entero por consola.
        Repite la solicitud hasta recibir un valor válido mayor o igual al mínimo indicado.
    Parámetros:
        Texto que se muestra al usuario al pedir el dato.
        Valor mínimo aceptado (por defecto es 1).
    Retorno:
        El número entero (válido) ingresado por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor
        except ValueError:
            # int() lanza ValueError si el valor ingresado por el usuario no es un número
            print("Ingresá un número entero válido.")

def pedir_texto(mensaje):
    """
    Función:
        Solicita al usuario que ingrese una cadena de texto no vacía por consola.
        Repite la solicitud si el usuario no escribe nada o ingresa solo espacios.
    Parámetros:
        Texto que se muestra al usuario al pedir el dato.
    Retorno:
        La cadena de texto (válida) ingresada por el usuario.
    """
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este campo no puede estar vacío.")

# 1 - AGREGAR PAÍS
def agregar_pais(paises):
    """Solicita los datos de un nuevo país y lo agrega a la lista."""
    print("\n─── Agregar país ───")
    nombre     = pedir_texto("Nombre del país   : ")
    continente = pedir_texto("Continente        : ")
    poblacion  = pedir_entero("Población         : ")
    superficie = pedir_entero("Superficie (km²)  : ")
    # Verificamos que no exista ya un país con el mismo nombre (sin distinguir mayúsculas)
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"\nYa existe un país llamado '{nombre}'.")
            return
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    print(f"\nPaís '{nombre}' agregado correctamente.")

# 2 - ACTUALIZAR PAÍS
def actualizar_pais(paises):
    """Actualiza la población y la superficie de un país existente."""
    print("\n─── Actualizar país ───")
    nombre = pedir_texto("Nombre del país a actualizar: ")
    for pais in paises:
        # Comparamos en minúsculas para no distinguir entre "argentina" y "Argentina"
        if pais["nombre"].lower() == nombre.lower():
            print(f"\nPaís encontrado: {pais['nombre']}")
            print(f"Población actual : {pais['poblacion']:,}")
            print(f"Superficie actual: {pais['superficie']:,} km²")
            # Sobreescribimos directamente los valores del diccionario
            pais["poblacion"]  = pedir_entero("Nueva población: ")
            pais["superficie"] = pedir_entero("Nueva superficie (km²): ")
            print(f"\nDatos de '{pais['nombre']}' actualizados correctamente.")
            return
    print(f"\nNo se encontró ningún país con el nombre '{nombre}'.")

# 3 - BUSCAR PAÍS
def buscar_pais(paises):
    """Busca países cuyo nombre contenga el texto ingresado (coincidencia parcial o exacta)."""
    print("\n─── Buscar país ───")
    termino = pedir_texto("Ingresá el nombre o parte del nombre: ")
    # Filtramos usando el operador "in" para permitir búsqueda parcial, sin distinguir mayúsculas
    resultados = [p for p in paises if termino.lower() in p["nombre"].lower()]
    if resultados:
        print(f"\nSe encontraron {len(resultados)} resultado(s):\n")
        mostrar_tabla(resultados)
    else:
        print(f"\nNo se encontraron países que coincidan con '{termino}'.")

# 4 - FILTRAR PAÍSES
def filtrar_paises(paises):
    """Muestra un submenú persistente para filtrar países por distintos criterios."""
    while True: #Utilizamos un ciclo while True para mostrar un submenu persistente
        print("\n─── Filtrar países ───")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("4. Volver al menú principal")
        opcion = input("\nSeleccioná una opción: ").strip()
        if opcion == "1":
            _filtrar_por_continente(paises)
        elif opcion == "2":
            _filtrar_por_poblacion(paises)
        elif opcion == "3":
            _filtrar_por_superficie(paises)
        elif opcion == "4":
            break
        else:
            print("\nOpción inválida.")

def _filtrar_por_continente(paises):
    continente = pedir_texto("Continente: ")
    # Comparamos en minúsculas para no distinguir "america" de "America"
    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
    _mostrar_filtro(resultados, f"continente '{continente}'")

def _filtrar_por_poblacion(paises):
    print("Ingresá el rango de población:")
    minimo = pedir_entero("Mínimo: ", minimo=0)
    maximo = pedir_entero("Máximo: ", minimo=0)
    if minimo > maximo:
        print("\nEl mínimo no puede ser mayor que el máximo.")
        return
    # Seleccionamos los países cuya población esté dentro del rango indicado
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    _mostrar_filtro(resultados, f"población entre {minimo:,} y {maximo:,}")

def _filtrar_por_superficie(paises):
    print("Ingresá el rango de superficie (km²):")
    minimo = pedir_entero("Mínimo: ", minimo=0)
    maximo = pedir_entero("Máximo: ", minimo=0)
    if minimo > maximo:
        print("\nEl mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    _mostrar_filtro(resultados, f"superficie entre {minimo:,} y {maximo:,} km²")

def _mostrar_filtro(resultados, criterio):
    """Muestra los resultados de un filtro o un mensaje si no hay coincidencias."""
    if resultados:
        print(f"\n{len(resultados)} país/es encontrado(s) con {criterio}:\n")
        mostrar_tabla(resultados)
    else:
        print(f"\nNo se encontraron países con {criterio}.")

# 5 - ORDENAR PAÍSES
def ordenar_paises(paises):
    """Ordena y muestra los países según el criterio y el orden elegidos por el usuario."""
    while True:
        print("\n─── Ordenar países ───")
        print("Criterio:")
        print("1. Nombre")
        print("2. Población")
        print("3. Superficie")
        print("4. Volver al menú principal")
        criterio = input("\nSeleccioná el criterio: ").strip()
        if criterio == "1":
            clave, etiqueta = "nombre", "nombre"
        elif criterio == "2":
            clave, etiqueta = "poblacion", "población"
        elif criterio == "3":
            clave, etiqueta = "superficie", "superficie"
        elif criterio == "4":
            break
        else:
            print("\nCriterio inválido.")
            return
        while True:
            print("Orden: ")
            print("1. Ascendente")
            print("2. Descendente")
            print("3. Volver a ingresar el criterio de ordenamiento")
            orden = input("\nSeleccioná el orden: ").strip()
            if orden == "1":
                reverse, etiqueta_orden = False, "ascendente"
            elif orden == "2":
                reverse, etiqueta_orden = True, "descendente"
            elif orden == "3":
                break
            else:
                print("\nOrden inválido.")
                return
            # sorted() no modifica la lista original, devuelve una nueva lista ordenada
            # key indica el campo del diccionario a usar como criterio de comparación
            # reverse=True ordena de mayor a menor, reverse=False de menor a mayor
            ordenados = sorted(paises, key=lambda p: p[clave], reverse=reverse)
            print(f"\nPaíses ordenados por {etiqueta} ({etiqueta_orden}):\n")
            mostrar_tabla(ordenados)

# 6 - ESTADÍSTICAS
def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas generales del dataset."""
    print("\n─── Estadísticas ───")
    if not paises:
        print("\nNo hay países cargados para calcular estadísticas.")
        return
    # Extraemos solo los valores numéricos en listas separadas para operar con ellos
    poblaciones = [p["poblacion"]  for p in paises]
    superficies = [p["superficie"] for p in paises]
    # max() y min() con key permiten buscar el diccionario completo según un campo
    mas_poblado = max(paises, key=lambda p: p["poblacion"])
    menos_poblado = min(paises, key=lambda p: p["poblacion"])
    print(f"\nTotal de países: {len(paises)}")
    print(f"País más poblado: {mas_poblado['nombre']} ({mas_poblado['poblacion']:,} hab.)")
    print(f"País menos poblado: {menos_poblado['nombre']} ({menos_poblado['poblacion']:,} hab.)")
    # :,.0f formatea el número con separador de miles y sin decimales
    print(f"Promedio de población: {statistics.mean(poblaciones):,.0f} hab.")
    print(f"Promedio de superficie: {statistics.mean(superficies):,.0f} km²")
    # Construimos un diccionario contando cuántos países hay por cada continente
    continentes = {}
    for p in paises:
        c = p["continente"]
        if c in continentes:
            continentes[c] = continentes[c] + 1
        else:
            continentes[c] = 1
    print(f"\nPaíses por continente:")
    for continente, cantidad in sorted(continentes.items()):
        print(f"{continente}: {cantidad}")

# FUNCIÓN AUXILIAR: MOSTRAR TABLA
def mostrar_tabla(paises):
    """Muestra una lista de países en formato de tabla con columnas alineadas."""
    # Los números dentro de <> y >  controlan el ancho y la alineación de cada columna
    encabezado = f"{'NOMBRE':<25} {'CONTINENTE':<15} {'POBLACIÓN':>15} {'SUPERFICIE (km²)':>18}"
    print(encabezado)
    print("  " + "─" * 75)
    for p in paises:
        # :, agrega separador de miles a los números (ej: 45,376,763)
        print(f"{p['nombre']:<25} {p['continente']:<15} {p['poblacion']:>15,} {p['superficie']:>18,}")
    print()

# MENU PRINCIPAL
def menu_principal():
    """Punto de entrada del sistema. Carga el CSV y despliega el menú en bucle."""
    print("=" * 50)
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("=" * 50)
    # Cargamos los datos al inicio; si el archivo no existe se empieza con lista vacía
    paises = cargar_paises(RUTA_CSV)
    while True:
        print("\n╔══════════════════════════════╗")
        print("║         MENÚ PRINCIPAL       ║")
        print("╠══════════════════════════════╣")
        print("║  1. Agregar país             ║")
        print("║  2. Actualizar país          ║")
        print("║  3. Buscar país              ║")
        print("║  4. Filtrar países           ║")
        print("║  5. Ordenar países           ║")
        print("║  6. Ver estadísticas         ║")
        print("║  7. Mostrar todos los países ║")
        print("║  8. Salir                    ║")
        print("╚══════════════════════════════╝")
        opcion = input("\nSeleccioná una opción: ").strip()
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            if paises:
                print(f"\n─── Todos los países ({len(paises)}) ───\n")
                mostrar_tabla(paises)
            else:
                print("\nNo hay países cargados.")
        elif opcion == "8":
            # Al salir guardamos todos los cambios en el CSV
            guardar_paises(RUTA_CSV, paises)
            print("\n¡Hasta luego!\n")
            break  # interrumpe el while True y termina el programa
        else:
            print("\nOpción inválida. Ingresá un número del 1 al 8.")
# PUNTO DE ENTRADA
# Este bloque garantiza que menu_principal() solo se ejecute
# cuando el archivo se corre directamente, no si se importa desde otro módulo
if __name__ == "__main__":
    menu_principal()