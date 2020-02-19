from argParser import args
from ConverterFactory import ConverterFactory

def main():

    obj = ConverterFactory()
    try:
        print(obj.getConverter())
    except Exception as e:
        print(e)

main()

