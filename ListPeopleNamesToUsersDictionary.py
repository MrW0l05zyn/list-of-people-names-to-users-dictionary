import argparse
import sys

# variables
usersDictionary = []

# configuración de analizador
analizador = argparse.ArgumentParser(
    usage='%(prog)s [-n name] [-l list] [-o file]',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description="""examples:

    ./%(prog)s -n 'Elliot Alderson'
    ./%(prog)s -l list-people-names.txt
    ./%(prog)s -n 'Elliot Alderson' -o users-dictionary.txt
    ./%(prog)s -l list-people-names.txt -o users-dictionary.txt""",
    epilog=''
)
# argumentos de analizador
analizador.add_argument('-n', '--name', action='store', help='name of person, example: \'Elliot Alderson\' (first name and last name)', dest='name', type=str)
analizador.add_argument('-l', '--list', action='store', help='list of people names, example: list-people-names.txt', dest='list', type=argparse.FileType('r'))
analizador.add_argument('-o', '--output', action='store', help='output users dictionary, example: users-dictionary.txt', dest='file', type=str)
analizador.add_argument('-V', '--version', action='version', version='Version: 0.2')

# lectura de argumentos desde linea de comandos
argumentos = analizador.parse_args()

# validación de ingreso de parámetros --name o --list
if not argumentos.name and not argumentos.list:
   analizador.print_help()

def ListPeopleNamesToUsersDictionary(nombre, apellido):
    usersDictionary.append(nombre)                      #elliot
    usersDictionary.append(apellido)                    #alderson

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

# argumento -n --name
if argumentos.name:
    persona = argumentos.name.lower().split()
    # validación de nombre y apellido
    if len(persona) == 2:
        ListPeopleNamesToUsersDictionary(persona[0], persona[1])
    else:
        print('Format error: [-n/--name] Name of person, example: \'Elliot Alderson\' (first name and last name).')
        sys.exit()

# argumento -l --list
if argumentos.list:
    archivo = argumentos.list
    for personas in archivo.readlines():
        persona = personas.lower().split()
        # validación de nombre y apellido
        if len(persona) == 2:
            ListPeopleNamesToUsersDictionary(persona[0], persona[1])
        else:
            print('Format error: [-n/--name] Name of person, example: \'Elliot Alderson\' (first name and last name).')
            sys.exit()
    archivo.close()

# guarda diccionario de usuario en archivo
if argumentos.file:
    usersDictionaryFile = open(argumentos.file,"w") 
    for userName in usersDictionary:
        usersDictionaryFile.write("{0}\n".format(userName))
    usersDictionaryFile.close()
else:
    # impresión de diccionario de usuarios
    for userName in usersDictionary:
        print(userName)