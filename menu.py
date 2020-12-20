# IMPORTS
import os


def menu(options, actions):
    os.system('clear' if os.name == 'posix' else 'cls')
    hr = "-" * (len(options) + 4)
    print(f'{hr}\n| {options} |\n{hr}')
    option = input('Escribe una opción: ')
    # PRUEBA
    func = actions.get(int(option), lambda: menu(options, actions))
    func()
