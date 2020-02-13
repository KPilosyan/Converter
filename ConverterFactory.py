from BinaryBase import BinaryBase
import os
import inspect
from argParser import args

class ConverterFactory:

    def getConverter(self, directory):
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                imported_module = __import__(directory + "." + filename[:-3], fromlist=filename[:-3])
                for i in dir(imported_module):
                    attribute = getattr(imported_module, i)
                    
                    if inspect.isclass(attribute) and inspect.isabstract(attribute) == False and attribute(args.val, args.fr, args.to).validateKeys() and attribute(args.val, args.fr, args.to).validateValue():
                        return attribute(args.val, args.fr, args.to).convert()
        return "Incorrect parameter(s)"
