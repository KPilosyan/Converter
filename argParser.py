import argparse

parser = argparse.ArgumentParser(usage='%(prog)s [-h] [-converters] [val] [-fr] [-to]')
parser.add_argument("-converters", required=False, help="Shows all the converters this program can operate")
parser.add_argument("val", type = str.lower, help="Amount that needs to be converted")
parser.add_argument("-fr", required=False, type = str.lower, help="Specifies from which metric system to convert the value")
parser.add_argument("-to", required=True, type = str.lower, help="Specifies to which metric system to convert the value")

args = parser.parse_args()

# TODO: ignore space [ lstrip() ] 
# TODO: --list_converters argument -> list of converters. amen converter arandzin describtion
#  TODO: discriptions of arguments

# TODO: add -h/--help argument to print info of all arguments, how to create new converter