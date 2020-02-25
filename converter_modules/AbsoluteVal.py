from BinaryBase import BinaryBase

class AbsoluteVal(BinaryBase):
    def validateValue(self):
        if self._val == "-0":
            raise Exception("No such thing as -0")
        try:
            float(self._val)
        except Exception:
            return False
        return True

    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("abs", "absolute")
        return _keywords

    def convert(self):
        return abs(float(self._val))
    
    def getInfo(self):
        return ("Returns the absolute value of the inserted number \nKeywords: "+ str(self.keywords()))