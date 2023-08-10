
#Funcion Title: Convierte en mayúscula el primer caracter luego de un espacio en blanco
multiline = """Facts about the Moon:\n There is no atmosphere.\n There is no sound."""
print(multiline.title())

#FUNCION PARA DIVIDIR UNA CADENA

#Funcion Split: Forma una lista a partir del texto. Sin argumento en el split asume que la separación es cada espacio en blanco
cadena = "La cadena de este este será divido por la función split"
cadena_list = cadena.split()
print(cadena_list)

#Si al split puedo colocarle un parámetro para que cada vez que ubique ese caracter haga la separacion y forme una lista

cadena = "En esta cadena vamos a separar por un caracter./n Esta será la lista"
cadena_list = cadena.split("/n")
print (cadena_list)

#FUNCIONES DE BÚSQUEDA DE CADENAS
# FUNCIÓN IN: Para saber si un texto se encuentra dentro de otro texto. Devuelve true o false
# Tener en cuenta que Python distingue de mayúsculas y minúsculas.

cadena = "Esta es una cadena de prueba para probar la función IN"   
print("probar" in cadena)

#Función find: para encontrar un texto en otro texto. Devuelve la posición donde se encuentra el texto. Si no encuentra devuelve -1.
cadena = "Esta es una cadena de prueba para probar la función find"
print(cadena.find("encuentra"))
print(cadena.find("cadena"))

#Función count: Sirve para contar cuántas veces hay una palabra en una cadena. Si no encuentra devuelve -1
cadena = "Esta es una cadena de ejemplo para probar la función count."
print(cadena.count("ejemplo"))

#Funcion lower: Convierte el texto en minúsculas

cadena="Este es una cadena para poder probar la FUNCIÓN lower"
print(cadena.lower())

#Funcion upper: Convierte el texto en minúsculas

cadena="Este es una cadena para poder probar la FUNCIÓN upper"
print(cadena.upper())

#COMPROBACIÓN DE CONTENIDO
#HAY OCASIONES EN LA QUE SE NECESITARÁ BUSCAR UN TEXTO DENTRO DE UNA CADENA E IMPRIMIR EL TEXTO ENCONTRADO
#POR EJEMPLO SI QUIERO IMPRIMIR LA NOTA DEL ALUMNO QUE ESTÁ DENTRO DE UN TEXTO PUEDO HACERLO CON SPLIT

cadena= "El profesor publicó la nota el miércoles 3 de julio. La nota del del alumno Diaz en el curso de matemática sabiendo que es la segunda vez que lo lleva es de: 10 "
cadena_split= cadena.split(":")
print(cadena_split[-1]) #En este caso la función confía que en la cadena solo hay dos puntos que separan la oración de la nota
#El -1 dentro del Split quiere decir que devuelva el último valor de la lista.

#Habrá situaciones en donde la cadena no tenga un caracter que distinga la separación y así poder armar una lista como en el ejemplo anterior.
#En ese caso se debe usar otras formas como la que sigue

cadena = "La temperatura del horno de barro debe llegar a 200 grados celcius. Y la temperatura de la refrigearadora tiene que estar en -5c"
for item in cadena.split():
    if item.isnumeric():
        print(item)

#En la cadena anterior -5 no lo reconoce como nro. Para eso se peden usar otras funcions como starswith y endswith

cadena = "La temperatura del horno de barro debe llegar a 200 grados celcius. Y la temperatura de la refrigearadora tiene que estar en -5c"
for item in cadena.split():
    if item.isnumeric():
        print(item)
    elif item.startswith("-"):
        print(item)

#O también así

cadena = "La temperatura del horno de barro debe llegar a 200 grados celcius. Y la temperatura de la refrigearadora tiene que estar en -5c"
for item in cadena.split():
    if item.isnumeric():
        print(item)
    elif item.endswith("c"):
        print(item)

#FUNCIONES DE REEMPLAZO DE TEXTO
cadena="La temperatura en el horno llega a 200 grados celcius mientras que la refrigeradora llega a -10 grados celcius"
print(cadena.replace("celcius","c"))