import argparse

# configuración de argumentos de linea de comandos
parser = argparse.ArgumentParser(
    usage='%(prog)s <list>',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Example: ./%(prog)s list-people-names.txt',
    epilog=''
)
parser.add_argument('<list>', action='store', help='list of people names')
parser.add_argument('-v', '--version', action='version', version='Version: 0.1')

# lectura de argumentos desde linea de comandos
parser.parse_args()