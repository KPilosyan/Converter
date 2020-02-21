from BinaryBase import BinaryBase
import os
import inspect
from argParser import args

class ConverterFactory:
    def getConvertersList(self):
        converters_list = []
        directory = "converter_modules"
        for filename in os.listdir(directory):
            if filename.endswith(".py"):   #filter .py files
                imported_module = __import__(directory + "." + filename[:-3], fromlist=filename[:-3])  #delete '.py' part of module name
                for i in dir(imported_module):
                    attribute = getattr(imported_module, i)

                    if inspect.isclass(attribute) and not inspect.isabstract(attribute) and issubclass(attribute, BinaryBase):
                        converters_list.append(attribute)
                    
        return converters_list

        """ Goes through the mentioned directory and opens each file one by one with the first loop
        and keeps the modules in variable 'imported_module'. Then second loop goes through all attributes in the module 
        and filters only classes that are not abstract and are inherited from 'BinaryBase' class.
            returns names of those classes as a list."""

    def getConverter(self):
        for attribute in self.getConvertersList():
            if attribute(args.val, args.fr, args.to).validateKeywords():  
                if attribute(args.val, args.fr, args.to).validateValue():
                    return attribute(args.val, args.fr, args.to).convert()
                else:
                    raise Exception("Invalid value input")
        else:
            raise Exception("Invalid parameter(s)")  
        
        """ Goes through 'GetConvertersList', finds the right converter by using validate functions of each class 
        and passes input parameters to convert(). In case of wrong user input(s), throws the according error"""
                                
        

    
        
