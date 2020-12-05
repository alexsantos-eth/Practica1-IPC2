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
        self.main_menu = menu('(1) Lectura  | (2) Cálculo | (3) Generación | (4) Salir/Información', {
            1: self.set_file,
            2: self.set_data,
            3: self.write_output,
            4: self.greeting
        })

    # OPCIONES
    def set_file(self):
        self.csv_file = csv_reader()
        self.init_menu()

    # GENERAR DICCIONARIO
    def set_data(self):
        if(self.csv_file != None):
            self.json_dict = compute_data(self.csv_file.get_matrix())

        # REGRESAR
        self.init_menu()

    # GENERAR JSON
    def write_output(self):
        if(self.json_dict != None):
            # ESCRIBIR
            with open('result.json', 'w') as fp:
                json.dump(self.json_dict.get_dict(), fp)

        # REGRESAR
        self.init_menu()

    def greeting(self):
        print(
            'GRACIAS POR USAR MI PROGRAMA, VISITA MI GITHUB https://github.com/alexsan-dev')


if __name__ == "__main__":
    main()
