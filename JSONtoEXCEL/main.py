import json
import os
import pandas as pd
import datetime

ruta = r'C:\Users\Alumno\Desktop\JSONtoEXCEL\employees.json'
ano = datetime.datetime.today().year
mes = datetime.datetime.today().month
salario = []
edad = []
nombre = []
genero = []
proyecto = []
email = []

if os.path.exists(ruta) and os.path.getsize(ruta) > 0:
    with open(ruta, 'r') as json_file:
        datos = json.load(json_file)
        for persona in datos:
            if persona['proyect'] != "GRONK":
                persona['salary'] = persona['salary'][1:].replace(',', '')

                if persona['age'] < 30:
                    persona['salary'] = (float(persona['salary'])) + (float(persona['salary']) * 10 / 100)

                salario.append(str(persona['salary']) + "€")
                edad.append(persona['age'])
                nombre.append(persona['name'])
                genero.append(persona['gender'])
                proyecto.append(persona['proyect'])
                email.append(persona['email'])

df = pd.DataFrame({'Nombre': nombre, 'Edad': edad, 'Genero': genero, 'Email': email,'Salario': salario, 'Proyecto': proyecto})
df.to_excel(f'pagos-empleados-{mes}-{ano}.xlsx')

