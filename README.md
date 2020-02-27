# List of people names to users dictionary

Herramienta que permite generar a partir de una lista de nombres de personas un diccionario de usuarios, basándose en convenciones de nomenclaturas típicas, utilizadas por los administradores de sistemas (SysAdmin) al momento de crear cuentas de usuario.

## Uso
```
ListPeopleNamesToUsersDictionary.py {list} [-o file]
```

## Ejemplos de utilización
```
python3 ./ListPeopleNamesToUsersDictionary.py list-people-names.txt
python3 ./ListPeopleNamesToUsersDictionary.py list-people-names.txt -o users-dictionary.txt
```

## Argumentos posicionales
```
  <list>         list of people names
```

## Argumentos opcionales
```
  -h, --help     show this help message and exit
  -o FILE        output users dictionary
  -V, --version  show program's version number and exit
```

## Ejemplo:

* Entrada: 

`Elliot Alderson`
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
