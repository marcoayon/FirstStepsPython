#Creamos un diccionario para almacenar nombres y edad
persona={
    'nombre':'Marco',
    'paterno':'Diaz',
    'materno':'Ayon',
    'edad':49
}

#El método get se usa para acceder al valor de una clave    

print(persona.get('nombre'))

#otra forma de acceder a los valores es usando los corchetes, esta forma es la mas usada por que usa menos código que get

print(f'Su nombre es {persona["nombre"]} su apellido paterno es {persona["paterno"]} y su apellido materno es {persona["materno"]}.'
      f' Esta persona tiene la edad de {persona["edad"]} años')

#Agregamos mas variables al diccionario
persona["distrito"]="Surco"
persona["departamento"]="Lima"
print(f'Su nombre es {persona["nombre"]} su apellido paterno es {persona["paterno"]} y su apellido materno es {persona["materno"]}.'
      f' Esta persona tiene la edad de {persona["edad"]} años. Vive en el distrito de {persona["distrito"]}.'
      f' Ubicado en departamento de {persona["departamento"]}.')

#Actualizamos los valodes de las variables de diccionario
persona["nombre"]="Sueli"
persona["distrito"]="La Molina"
persona["edad"]="45"

print(f'Su nombre es {persona["nombre"]} su apellido paterno es {persona["paterno"]} y su apellido materno es {persona["materno"]}.'
      f' Esta persona tiene la edad de {persona["edad"]} años. Vive en el distrito de {persona["distrito"]}.'
      f' Ubicado en departamento de {persona["departamento"]}.')

#Otra forma de actualizar  los valores de los campos de un diccionario usando update.
persona.update({
    "nombre":"Pierre",
    "edad":"40",
    "distrito":"Seatle",
    "ciudad":"Washington"
})
print(f'Su nombre es {persona["nombre"]} su apellido paterno es {persona["paterno"]} y su apellido materno es {persona["materno"]}.'
      f' Esta persona tiene la edad de {persona["edad"]} años. Vive en el distrito de {persona["distrito"]}.'
      f' Ubicado en departamento de {persona["departamento"]}.')

#Agregamos diccionarios dentro de un diccionario

persona['residencia']={
    'distrito':'Ate',
    'departamento':'Lima'
}

print(f'Su nombre es {persona["nombre"]} su apellido paterno es {persona["paterno"]} y su apellido materno es {persona["materno"]}.'
      f' Esta persona tiene la edad de {persona["edad"]} años. Vive en el distrito de {persona["residencia"]["distrito"]}.'
      f' Ubicado en departamento de {persona["residencia"]["departamento"]}.')

#Para eliminar un campo del diccionario se usa pop
persona.pop("distrito")

#El uso del método keys() usado para recuperar todos los valores de un diccionario

lista = {
    'Marco' : 49,
    'Eduardo': 50,
    'Rogger' : 41,
    'Luis' : 27,
    'Edgar' : 31
}
for key in lista.keys():
    print(f'{key} tiene la edad de {lista[key]} años')

#Para poder encontrar un key dentro del diccionario se usa el método in    

if 'Eduardo' in lista:
    lista['Eduardo'] = lista['Eduardo'] + 1
else:
    lista['Eduardo'] = 45     

for nombre in lista.keys():
    if nombre == 'Eduardo':
        print(f'Ahora la edad de {nombre} es de {lista["Eduardo"]}')

"""
Ejercicio en donde debo crear una lista de alumnos con sus respectivas notas para luego listar la cantidad de alumnos 
y luego debo saber el promedio simple de los alumnos
"""

print('=======================================================================================')
print('=======================================================================================')

listaalumnos = {
    'Sandra' : 14.55,
    'Mafer' : 16.24,
    'Fabiana' : 15.64,
    'Marco' : 14.87,
    'Rosa' : 10.25,
    'Jesus' : 12.64,
    'Renato' : 14.72,
    'Sueli' : 15.31,
    'Gino' : 14.17,
    'Gino Paolo' : 16.72
}
suma_nota = 0


for alumno in listaalumnos.keys():
    print(f'La nota del alumno(a) {alumno} es {listaalumnos[alumno]}')
    suma_nota = suma_nota + listaalumnos[alumno]

print(f'El promedio del aula es {suma_nota / len(listaalumnos.keys())}')

#Otra forma de calcular el promedio del salon es:
suma_nota = 0
notas = listaalumnos.values() #Con este método obtengo los valores asignados a cada key y se crea una lista
for nota in notas:
    suma_nota = suma_nota + nota

total_alumno = len(listaalumnos.keys())

print(f'El promedio del salón es {suma_nota / total_alumno}')

