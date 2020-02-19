from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return float(self._val)
        
    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("inv", "inverse")
        return _keywords

    def convert(self):
        if self._val != 0:
            return 1/int(self._val)
        raise Exception("Can't divide by 0")

    def getInfo(self):
        return 
        

    