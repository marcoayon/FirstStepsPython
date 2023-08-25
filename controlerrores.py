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
# Dentro del except pongo "Exception" para controlar cualquier error pero el mensaje es genérico

def main_varioserroresespecificos():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
#=======================FIN VARIOS ERRORES ESPECÍFICOS=================================

#=======================INICIO VARIOS ERRORES ESPECÍFICOS EN UNA SOLA EXCEPCION==============================
# Dentro del except pongo "Exception" para controlar cualquier error pero el mensaje es genérico

def main_varioserroresespecificos():
    try:
        configuration = open('config.txt')
    except (FileNotFoundError,PermissionError):
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
#=======================FIN VARIOS ERRORES ESPECÍFICOS EN UNA SOLA EXCEPCION=================================

if __name__ == '__main__':
    #main_errorfilenoencontrado()
    #main_errorespecifico()
    main_varioserroresespecificos()

