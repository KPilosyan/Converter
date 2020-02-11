from BinaryBase import BinaryBase
import os
import inspect

class ConverterFactory:
    def __init__(self, fr, to):
        self.fr = fr
        self.to = to

    def getBinaryConverter(self):
        try:
            directory = 'binary_modules'
            for filename in os.listdir(directory):
                if filename.endswith(".py"):
                    imported_module = __import__(directory + "." + filename[:-3], fromlist=filename[:-3])
                    print(imported_module)
                    for i in dir(imported_module):
                        attribute = getattr(imported_module, i)
                        if inspect.isclass(attribute) and issubclass(attribute, BinaryBase) and attribute.validateKeys():
                            return attribute
                    return "Error!"

        except Exception as e:
            print(e)
        
    def getUnaryConverter(self):
        try:
            directory = 'unary_modules'
            for filename in os.listdir(directory):
                if filename.endswith(".py"):
                    imported_module = __import__(directory + "." + filename[:-3], fromlist=filename[:-3])
                    print(imported_module)
                    for i in dir(imported_module):
                        attribute = getattr(imported_module, i)
                        if inspect.isclass(attribute) and issubclass(attribute, BinaryBase) and attribute.validateKeys():
                            return attribute
                    return "Error!"
        except Exception as e:
            print(e)

     


        