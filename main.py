# IMPORTS
import json
from menu import menu
from csv import csv_reader
from compute import compute_data

# GLOBALES


class main():
    def __init__(self):
        # GLOBALES
        self.csv_file = None
        self.json_dict = None
        self.init_menu()

    # MENU PRINCIPAL
    def init_menu(self):
        self.main_menu = menu('(1) Lectura de archivo CSV  | (2) Cálculo de Datos | (3) Generación de archivo JSON | (4) Información', {
            1: self.set_file,
            2: self.set_data,
            3: self.write_output,
            4: self.greeting
        })

    # OPCIONES
    def set_file(self):
        self.csv_file = csv_reader()
        self.init_menu()

    def set_data(self):
        self.json_dict = compute_data(self.csv_file.get_matrix())
        self.init_menu()

    def write_output(self):
        with open('result.json', 'w') as fp:
            json.dump(self.json_dict.get_dict(), fp)

        # REGRESAR
         self.init_menu()

    def greeting(self):
        print(
            'GRACIAS POR USAR MI PROGRAMA, VISITA MI GITHUB https://github.com/alexsan-dev')
        self.init_menu()


if __name__ == "__main__":
    main()
