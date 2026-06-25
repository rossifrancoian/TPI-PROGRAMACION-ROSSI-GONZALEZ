# Sistema de Gestión de Países
## Descripción
Este proyecto consiste en una aplicación de consola desarrollada en Python para la gestión de información de países almacenada en un archivo CSV.
El sistema permite realizar operaciones de carga, consulta, actualización, filtrado, ordenamiento y análisis estadístico sobre un conjunto de países, utilizando estructuras de datos nativas de Python y persistencia mediante archivos CSV.
Los datos almacenados para cada país son:

* Nombre
* Población
* Superficie (km²)
* Continente

## Requisitos
* Python 3.8 o superior
* Archivo `paises.csv` ubicado en la misma carpeta que el programa

## Estructura del Proyecto
proyecto/
│
├── main.py
├── paises.csv
└── README.md

## Formato del Archivo CSV
El archivo `paises.csv` debe contener los siguientes encabezados:

nombre,poblacion,superficie,continente
Argentina,46044703,2780400,América
Brasil,212559417,8515767,América
España,47351567,505990,Europa

## Funcionalidades
### 1. Agregar país
Permite registrar un nuevo país indicando:
* Nombre
* Continente
* Población
* Superficie
El sistema verifica que no exista previamente un país con el mismo nombre.

### 2. Actualizar país
Permite modificar:
* Población
* Superficie de un país existente.

### 3. Buscar país
Realiza búsquedas por coincidencia total o parcial del nombre.

### 4. Filtrar países
Permite filtrar por:
* Continente
* Rango de población
* Rango de superficie

### 5. Ordenar países
Permite ordenar la información por:
* Nombre
* Población
* Superficie
En orden:
* Ascendente
* Descendente

### 6. Estadísticas
Calcula:
* Cantidad total de países
* País más poblado
* País menos poblado
* Promedio de población
* Promedio de superficie
* Cantidad de países por continente

### 7. Mostrar todos los países
Visualiza el contenido completo del dataset en formato tabular.

### 8. Guardado automático
Al salir del programa, todos los cambios realizados se guardan automáticamente en el archivo CSV.

## Ejecución del Programa
Desde una terminal ubicada en la carpeta del proyecto:
python main.py
o
python3 main.py
según la instalación de Python.

## Ejemplos de Uso
### Ejemplo 1: Agregar un país
**Entrada**
Seleccioná una opción: 1
Nombre del país   : Uruguay
Continente        : América
Población         : 3500000
Superficie (km²)  : 176215

**Salida**
País 'Uruguay' agregado correctamente.

### Ejemplo 2: Buscar un país
**Entrada**
Seleccioná una opción: 3
Ingresá el nombre o parte del nombre: arg

**Salida**
Se encontraron 1 resultado(s):
NOMBRE                    CONTINENTE          POBLACIÓN   SUPERFICIE (km²)
---------------------------------------------------------------------------
Argentina                 América           46,044,703         2,780,400


### Ejemplo 3: Ver estadísticas
**Entrada**
Seleccioná una opción: 6
**Salida**
Total de países: 3
País más poblado: Brasil (212,559,417 hab.)
País menos poblado: Uruguay (3,500,000 hab.)
Promedio de población: 87,368,040 hab.
Promedio de superficie: 3,157,460 km²

Países por continente:
América: 3

## Manejo de Errores
El sistema contempla:
* Archivo CSV inexistente.
* Errores de formato en el CSV.
* Ingreso de valores no numéricos.
* Campos vacíos.
* Opciones inválidas de menú.
* Rangos incorrectos en filtros.
* Búsquedas sin resultados.

## Tecnologías Utilizadas
* Python
* Módulo `csv`
* Módulo `statistics`
* Manejo de excepciones (`try/except`)
* Listas
* Diccionarios
* Comprensión de listas
* Funciones modulares
* Estructuras secuenciales, condicionales y repetitivas

## Participación de Integrantes
### Integrante 1
* Nombre: Gonzalez Nahir Evelyn
* Legajo:19203
* Tareas realizadas: Funciones de validaciones (funcion de pedir entero, pedir texto), de agregar pais,  de filtrar paises, de mostrar estadisticas, para mostrar la tabla. Tambien se encargo de realizar los docstrings de cada una de las funciones. 

### Integrante 2
* Nombre: Rossi Franco Ian
* Legajo:19296
* Tareas realizadas: Funciones de archivo CSV (funcion de Cargar y Guardar paises), de actualizar pais, de buscar pais, de ordenar paises, una para el menu principal, ademas de crear el CSV con una base previa cargada. Archivo readme.md. 

## Autoría
Trabajo práctico académico desarrollado para la gestión y análisis de información de países utilizando Python y archivos CSV.
