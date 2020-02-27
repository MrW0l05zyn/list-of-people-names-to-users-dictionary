import argparse

# variables
usersDictionary = []

# configuración de argumentos de linea de comandos
analizador = argparse.ArgumentParser(
    usage='%(prog)s <list>',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Example: ./%(prog)s list-people-names.txt',
    epilog=''
)
analizador.add_argument('list', action='store', help='list of people names', type=argparse.FileType('r'))
analizador.add_argument('-v', '--version', action='version', version='Version: 0.1')

# lectura de argumentos desde linea de comandos
argumentos = analizador.parse_args()
archivo = argumentos.list

# lectura de lista de nombres de personas
for personas in archivo.readlines():
    persona = personas.lower().split()
    nombre = persona[0]         #elliot
    apellido = persona[1]       #alderson

    usersDictionary.append(nombre + apellido)           #elliotalderson
    usersDictionary.append(apellido + nombre)           #aldersonelliot

    usersDictionary.append(nombre + '.' + apellido)     #elliot.alderson
    usersDictionary.append(apellido + '.' + nombre)     #alderson.elliot
    usersDictionary.append(nombre + '_' + apellido)     #elliot_alderson
    usersDictionary.append(apellido + '_' + nombre)     #alderson_elliot
    usersDictionary.append(nombre + '-' + apellido)     #elliot-alderson
    usersDictionary.append(apellido + '-' + nombre)     #alderson-elliot

    usersDictionary.append(nombre + apellido[0])        #elliota
    usersDictionary.append(apellido + nombre[0])        #aldersone
    usersDictionary.append(nombre[0] + apellido)        #ealderson
    usersDictionary.append(apellido[0] + nombre)        #aelliot

    usersDictionary.append(nombre + '.' + apellido[0])  #elliot.a
    usersDictionary.append(apellido + '.' + nombre[0])  #alderson.e
    usersDictionary.append(nombre + '_' + apellido[0])  #elliot_a
    usersDictionary.append(apellido + '_' + nombre[0])  #alderson_e
    usersDictionary.append(nombre + '-' + apellido[0])  #elliot-a
    usersDictionary.append(apellido + '-' + nombre[0])  #alderson-e

    usersDictionary.append(nombre[0] + '.' + apellido)  #e.alderson
    usersDictionary.append(apellido[0] + '.' + nombre)  #a.elliot
    usersDictionary.append(nombre[0] + '_' + apellido)  #e_alderson
    usersDictionary.append(apellido[0] + '_' + nombre)  #a_elliot
    usersDictionary.append(nombre[0] + '-' + apellido)  #e-alderson
    usersDictionary.append(apellido[0] + '-' + nombre)  #a-elliot

    usersDictionary.append(nombre)                      #elliot
    usersDictionary.append(apellido)                    #alderson
archivo.close()

# impresión de usernames
for userName in usersDictionary:
    print(userName)