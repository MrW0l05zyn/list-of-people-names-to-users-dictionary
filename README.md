# List of people names to users dictionary

Herramienta que permite generar a partir de una lista de nombres de personas un diccionario de usuarios, basándose en convenciones de nomenclaturas típicas, utilizadas por los administradores de sistemas (SysAdmin) al momento de crear cuentas de usuario.

Usage:
```
ListPeopleNamesToUsersDictionary.py {list} [-o file]
```

Example:
```
python3 ./ListPeopleNamesToUsersDictionary.py list-people-names.txt
python3 ./ListPeopleNamesToUsersDictionary.py list-people-names.txt -o users-dictionary.txt
```

Positional arguments:
```
  <list>         list of people names
```
Optional arguments:
```
  -h, --help     show this help message and exit
  -o FILE        output users dictionary
  -V, --version  show program's version number and exit
```
