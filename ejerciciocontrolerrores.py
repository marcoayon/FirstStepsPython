loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

diccionario = {}
for item in loaded_config.split('\n'):
    try:
        llave, valor=item.split('=')
        diccionario[llave]= valor
    except ValueError:
        print(f'No se puede analizar{item}')

print (diccionario)




    