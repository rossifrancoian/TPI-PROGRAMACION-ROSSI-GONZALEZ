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