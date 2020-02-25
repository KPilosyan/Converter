import argparse

parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-converters] [-val] [-fr] [-to]')
parser.add_argument("-converters", action='store_true', help="Shows all the converters this program can operate")
parser.add_argument("-val", type = str.lower, help="Amount that needs to be converted")
parser.add_argument("-fr", type = str.lower, help="Specifies from which metric system to convert the value")
parser.add_argument("-to", type = str.lower, help="Specifies to which metric system to convert the value")

args = parser.parse_args()
