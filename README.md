# List of people names to users dictionary

Herramienta que permite generar a partir de una lista de nombres de personas un diccionario de usuarios, basándose en convenciones de nomenclaturas típicas, utilizadas por los administradores de sistemas (SysAdmin) al momento de crear cuentas de usuario.

## Ejemplo

* Entrada: 

```
Elliot Alderson
```

* Salida:

```
elliot
alderson
elliotalderson
aldersonelliot
elliot.alderson
alderson.elliot
elliot_alderson
alderson_elliot
elliot-alderson
alderson-elliot
elliota
aldersone
ealderson
aelliot
elliot.a
alderson.e
elliot_a
alderson_e
elliot-a
alderson-e
e.alderson
a.elliot
e_alderson
a_elliot
e-alderson
a-elliot
```

## Uso
```
ListPeopleNamesToUsersDictionary.py [-n name] [-l list] [-o file]
```

## Ejemplos de utilización
```
./ListPeopleNamesToUsersDictionary.py -n 'Elliot Alderson'
./ListPeopleNamesToUsersDictionary.py -l list-people-names.txt
./ListPeopleNamesToUsersDictionary.py -n 'Elliot Alderson' -o users-dictionary.txt
./ListPeopleNamesToUsersDictionary.py -l list-people-names.txt -o users-dictionary.txt
```

## Argumentos
```
  -h, --help             show this help message and exit
  -n NAME, --name NAME   name of person, example: 'Elliot Alderson' (only first name and last name)
  -l LIST, --list LIST   list of people names, example: list-people-names.txt
  -o FILE, --output FILE output users dictionary, example: users-dictionary.txt
  -V, --version          show program's version number and exit
```
