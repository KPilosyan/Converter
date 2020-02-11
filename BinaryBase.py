from abc import ABC, abstractmethod 

class BinaryBase(ABC):
    def __init__(self, val, fr, to):
        self._val = val
        self.fr = fr
        self.to = to

    @abstractmethod
    def getKeys(self):
        return 

    @abstractmethod
    def validateValue(self):
        return 

    @abstractmethod
    def validateKeys(self):
        return 
            
    @abstractmethod
    def convert(self):
        return 

