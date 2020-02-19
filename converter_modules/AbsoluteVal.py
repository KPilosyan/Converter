from BinaryBase import BinaryBase

class AbsoluteVal(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("abs", "absolute")
        return _keywords

    def convert(self):
        return abs(int(self._val))
    
    def getInfo(self):
        return ("Returns the absolute value of the inserted number \nKeywords: "+ str(self.keywords()))