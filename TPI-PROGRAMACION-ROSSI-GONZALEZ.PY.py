import csv
import statistics
import os

RUTA_CSV = "paises.csv"

# FUNCIONES DE ARCHIVO CSV
def cargar_paises(ruta):
    """Carga los países desde el archivo CSV y los devuelve como lista de diccionarios."""
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
    """Guarda la lista de países en el archivo CSV."""
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
    """Solicita un número entero al usuario hasta que ingrese uno válido."""
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
    """Solicita un texto no vacío al usuario."""
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
