import argparse

parser = argparse.ArgumentParser()
parser.add_argument("val", type = str.lower, help="Amount that needs to be converted")
parser.add_argument("-fr", required=False, type = str.lower, help="Specifies from which metric system to convert the value (Nonrequired argument)")
parser.add_argument("-to", required=True, type = str.lower, help="Specifies to which metric system to convert the value")
parser.add_argument("--list_of_converters", required=False, help="Shows all the converters this program can operate")

args = parser.parse_args()

# TODO: ignore space [ lstrip() ] 
# TODO: --list_converters argument -> list of converters. amen converter arandzin describtion
#  TODO: discriptions of arguments
# TODO: 1 directory instead of 2
# TODO: add -h/--help argument to print info of all arguments, how to create new converter