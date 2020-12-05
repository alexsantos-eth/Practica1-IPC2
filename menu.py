# IMPORTS
import os


class menu:
    # INICIAR MENU
    def __init__(self, options, actions):
        self.options = options
        self.actions = actions

        # CONTROLAR SALIDA
        self.init_menu()

    # INICIAR MENU
    def init_menu(self):
        self.clean_screen()
        self.show_menu()
        self.set_option()

    # LIMPIAR PANTALLA
    def clean_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    # MOSTRAR OPCIONES
    def show_menu(self):
        hr = "-" * (len(self.options) + 4)
        print(f'{hr}\n| {self.options} |\n{hr}')

    # ASIGNAR ACCION
    def set_option(self):
        option = input('Escribe una opción: ')

        # LISTA DE OPCIONES
        func = self.actions.get(int(option),  self.init_menu)
        func()
