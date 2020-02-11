from argParser import args
from ConverterFactory import ConverterFactory

def main():

    if args.fr:
        a = ConverterFactory(args.val, args.fr, args.to)
        a.getBinaryConverter()
    else:
        a = ConverterFactory(args.val, args.fr, args.to)
        a.getUnaryConverter()

main()

