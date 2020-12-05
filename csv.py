# IMPORTS
from menu import menu
from main import main_menu


class csv_reader:
    def __init__(self):
        path = ''
        menu('(1) Leer archivo | (2) Regresar', {
            1: self.read_file,
            2: main_menu
        })

    def read_file(self):
        # PREGUNTAR
        self.path = input('Ingresa la ruta de tu archivo: ')
