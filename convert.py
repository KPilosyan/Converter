from argParser import args
from ConverterFactory import ConverterFactory

def main():

    if args.fr:
        directory = "binary_modules"
        bi = ConverterFactory()
        print(bi.getConverter(directory))
    else:
        directory = "unary_modules"
        un = ConverterFactory()
        print(un.getConverter(directory))

main()

