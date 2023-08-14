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


#Función con argumentos predeterminados
print('========FUNCIÓN CON ARGUMENTOS PREDETERMINADOS===================')
from datetime import timedelta,datetime

def calcula_horas(tiempo = 51):
    ahora = datetime.now()
    aterriza = ahora + timedelta(hours = tiempo)
    return aterriza.strftime("Aterriza: %A %H:%M")

print (calcula_horas())

print('========FUNCIÓN CON ARGUMENTOS SIN PREDETERMINAR Y ARGUMENTOS PREDETERMINADOS===================')

def calcula_aterrizaje(planeta, tiempo=51):
    ahora = datetime.now()
    aterriza = ahora + timedelta(hours=tiempo)
    return aterriza.strftime(f"Llegará a {planeta} el día : %A a las %H:%M")
    
print(calcula_aterrizaje('Luna'))

print('========EJERCICIO CON ARGUEMNTO DE VARIABLE===================')

#Un argumento variable permite recibir una cantidad de variables sin haberlos definido.
#para ello se debe anteponer un asterísco (*)

def argumento_variable(*variables):
    tiempo = sum(variables)
    if tiempo < 60:
        return f'El tiempo que falta es de {tiempo} minutos'
    else:
        return f'El tiempo que falta es de {tiempo/60} horas'

print(argumento_variable(15,10,6))
print(argumento_variable(15,60,6))

print('========EJERCICIO CON ARGUEMNTO DE PALABRA CLAVE VARIABLE===================')
#Para que un argumento acepte palabra clave variable debe usarse doble asterísco (**)

def argumento_palabraclave_variable(**argumento):
    print(f'La cantidad de tripulantes en el avión es de {len(argumento)} y está conformada por:')
    for titulo, nombre in argumento.items():
        print (f'{titulo}: {nombre}')

argumento_palabraclave_variable(Piloto='Marco',Flyhoster='Ariana')

