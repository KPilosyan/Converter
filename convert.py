from argParser import args
from ConverterFactory import ConverterFactory

def main():

    obj = ConverterFactory()
    if args.converters:
        for i in obj.getConvertersList():
            print("\n"+ i.__name__, "-->", i(args.val, args.fr, args.to).getInfo(), "\n")
        
    try:
        print(obj.getConverter())
    except Exception as e:
        print(e)

main()

