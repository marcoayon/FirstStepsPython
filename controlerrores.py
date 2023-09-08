#=======================INICIO EXCEPCION DE FILE NO ENCONTRADO==============================
# Dentro del except pongo el error FileNotFoundError para controlar el error especídico
# que el archivo no ha sido encontrado
def main_errorfilenoencontrado():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
#=======================FIN EXCEPCION DE FILE NO ENCONTRADO=================================

#=======================INICIO ERROR GENÉRICO==============================
# Dentro del except pongo "Exception" para controlar cualquier error pero el mensaje es genérico
def main_errorespecifico():
    try:
        configuration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")
#=======================FIN ERROR GENÉRICO=================================

#=======================INICIO VARIOS ERRORES ESPECÍFICOS==============================
# Dentro del except pongo "FileNotFoundError" para controlar que el archivo no se encuentra y pongo 
# "IsADirectoryError" para controlar que el directorio no existe
def main_varioserroresespecificos():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
#=======================FIN VARIOS ERRORES ESPECÍFICOS=================================

#=======================INICIO VARIOS ERRORES ESPECÍFICOS EN UNA SOLA EXCEPCION==============================
# En un mismo except puedo controlar varios errores, se debe poner entre parentesis
# Sugerencia : Aunque puede agrupar excepciones, solo debe hacerlo cuando no sea necesario controlarlas individualmente. 
# Evite agrupar muchas excepciones para proporcionar un mensaje de error generalizado.
def main_varioserroresespecificosenuna():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
#=======================FIN VARIOS ERRORES ESPECÍFICOS EN UNA SOLA EXCEPCION=================================

#=======================INICIO PARA INGRESAR AL DETALLE DEL ERROR==============================
#Para poder acceder al detalle del error se debe colocar un AS

def main_obtenereldetalledeleerror():
    try:
        open("mars.jpg")
    except FileNotFoundError as err:
        print("Got a problem trying to read the file:", err)
#=======================FIN PARA INGRESAR AL DETALLE DEL ERROR==============================


#=======================INICIO PARA INGRESAR AL DETALLE DEL ERROR==============================
#OSError 
def main_diferenciarelerrorconOsError():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    #main_errorfilenoencontrado()
    #main_errorespecifico()
    #main_varioserroresespecificos()
    #main_obtenereldetalledeleerror()
    main_diferenciarelerrorconOsError()

