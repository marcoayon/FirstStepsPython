#El uso de funciones

#Función sin argumento
def imprime_texto():
    print ('Este es un texto de prueba')

imprime_texto()

#Función con argumento

def calcula_tiempo_de_llegada(distancia, velocidad):
    tiempo = distancia / velocidad
    return tiempo

print(calcula_tiempo_de_llegada(10,50))

#Se  puede redondear el valor colocando directamente la función round llamando a la función
print('===============================================')
print(round(calcula_tiempo_de_llegada(10,50)))

#Un ejercicio donde envío como parametros 3 valores
print('===============================================')
def datos_diccionario(nombre,apellidopaterno,apellidomaterno,edad):
    datos_alumno = f''' El nombre es {nombre} el apellido paterno es {apellidopaterno} el apellido materno es {apellidomaterno}'''
    print (datos_alumno)

datos_diccionario('Marco', 'Diaz', 'Ayon',49)
