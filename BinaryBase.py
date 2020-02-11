from abc import ABC, abstractmethod 

class BinaryBase(ABC):
    def __init__(self, val, fr, to):
        self._val = val
        self.fr = fr
        self.to = to

    @abstractmethod
    def getKeys(self):
        pass

    @abstractmethod
    def validateValue(self):
        pass

    @abstractmethod
    def validateKeys(self):
        pass
            
    @abstractmethod
    def convert(self):
        pass

