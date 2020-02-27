from Base import Base

class AbsoluteVal(Base):
    def validateValue(self):
        if self._val == "-0":
            raise Exception("No such thing as -0")
        try:
            float(self._val)
        except Exception:
            return False
        return True

    def validateKeywords(self):
        if not self.fr:
            return self.to in self.keywords()
        raise Exception("Absolute value doesn't require argument 'fr'") 

    def keywords(self):
        _keywords = ("abs", "absolute")
        return _keywords

    def convert(self):
        return abs(float(self._val))
    
    def getInfo(self):
        return ("Returns the absolute value of the inserted number \nKeywords: "+ str(self.keywords()))