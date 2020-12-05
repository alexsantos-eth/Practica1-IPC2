# IMPORTS
from menu import menu
from csv import csv_reader

# GLOBALES
csv_file = None


# OPCIONES
def set_file():
    csv_file = csv_reader()


main_menu = menu('(1) Lectura de archivo CSV  | (2) Cálculo de Datos | (3) Generación de archivo JSON.', {
    1: set_file
})
