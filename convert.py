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

""" HOW IT WORKS"""
""" There are 2 types of inputs: Binary, Unary. User either inputs '[value] [-fr=keyword] [-to=keyword]' (Binary)
or '[value] [-to=keyword]' (Unary). Converter validates [value] and keywords, then returns conversion result.
i.e. 5 -fr=kg -to=g --> 5000; -5 -to=square --> 25. """

""" CREATING NEW CONVERTER """
""" Add .py file in 'converter_modules' directory with any name. The new class has to inherit from abstract class BinaryBase.
To see info about its abstract required methods look inside BinaryBase module. Make sure to override the required methods
for each new class, so that ConverterFactory will see and check its validate functions. If the validations return true, 
ConverterFactory will return the convert method of that class. 
The name of the class and its function getInfo() will be shown in command '-converters' as user info. """