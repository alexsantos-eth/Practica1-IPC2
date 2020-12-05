# IMPORTS
import os


def menu(options, actions):
    # LIMPIAR PANTALLA
    os.system('clear' if os.name == 'posix' else 'cls')

    # MOSTRAR OPCIONES
    hr = "-" * (len(options) + 4)
    print(f'{hr}\n| {options} |\n{hr}')

    # ASIGNAR ACCION
    option = input('Escribe una opción: ')

    # LISTA DE OPCIONES
    func = actions.get(int(option), lambda: menu(options, actions))
    func()
