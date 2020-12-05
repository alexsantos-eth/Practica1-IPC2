# IMPORTS
from menu import menu


class csv_reader:
    def __init__(self):
        # GLOBALES
        self.matrix = []
        self.path = ''

        # MENU
        menu('(1) Leer archivo | (2) Regresar', {
            1: self.read_file,
            2: lambda: None
        })

    def read_file(self):
        # PREGUNTAR
        self.path = input('Ingresa la ruta de tu archivo: ')

        # LEER
        reader = open(self.path)
        line_count = 0
        for line in reader:
            # CORTAR
            trim = line[0:-1]

            # AGREGAR
            if line_count > 0:
                self.matrix.append(trim.split(','))
            line_count += 1

        # CERRAR BUFFER
        reader.close()

    def get_matrix(self):
        return self.matrix
