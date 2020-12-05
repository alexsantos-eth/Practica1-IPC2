# IMPORTS
from menu import menu


class compute_data:
    def __init__(self, matrix):
        # GLOBALES
        self.matrix = matrix
        self.employees = {}
        self.summary = {}
        self.output = {}

        # MENU
        menu('(1) Cálcular datos | (2) Regresar', {
            1: self.set_dict,
            2: lambda: None
        })

    def set_dict(self):
       # ASIGNAR
        for row in self.matrix:
            self.employees[row[0]] = {
                'name': row[1],
                "last_name": row[2],
                'age': int(row[3]),
                'job': row[4],
                'cash': int(row[5])
            }

        # CALCULAR
        for key in self.employees:
            # LEER EDAD Y SALARIO
            age = self.employees[key]['age']
            wage = self.employees[key]['cash']

            # LEER EMPLEO
            job_key = self.employees[key]['job']
            job = self.summary.get(job_key, {
                'candidates': 0,
                'ages': [],
                'wages': []
            })

            # AGREGAR CANDIDATO, EDAD Y SALARIO
            job['candidates'] += 1
            job['ages'].append(int(age))
            job['wages'].append(int(wage))

            # ASIGNAR
            self.summary[job_key] = job

        # ASIGNAR VALORES DE SALIDA
        for key in self.summary:
            # LEER PROPIEDADES
            candidates = self.summary[key]['candidates']
            ages = self.summary[key]['ages']
            wages = self.summary[key]['wages']

            # ASIGNAR
            self.output[key] = {
                'candidates': candidates,
                'ages': sum(ages)/len(ages),
                'wages': sum(wages)/len(wages)
            }

    def get_dict(self):
        return self.output
