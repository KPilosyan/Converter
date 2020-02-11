from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()
        
    def validateKeys(self):
        return self.to in self.getKeys()

    def getKeys(self):
        keys = ("inv", "inverse")
        return keys

    def convert(self):
        return 1/self._val
        

    