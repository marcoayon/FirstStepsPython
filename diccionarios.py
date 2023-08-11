#Creamos un diccionario para almacenar nombres y edad
persona={
    'nombre':'Marco',
    'paterno':'Diaz',
    'materno':'Ayon',
    'edad':49
}
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
