import argparse

parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-converters] [-val] [-fr] [-to]')
subparsers = parser.add_subparsers()
parser.add_argument("-converters", action='store_true', help="Shows all the converters this program can operate")

convert = subparsers.add_parser('convert', help="Command name")
convert.add_argument("val", type = str.lower, help="Amount that needs to be converted")
convert.add_argument("-fr", type = str.lower, help="Specifies from which metric system to convert the value")
convert.add_argument("-to", required=True, type = str.lower, help="Specifies to which metric system to convert the value")

args = parser.parse_args()
