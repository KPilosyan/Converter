from BinaryBase import BinaryBase

class Square(BinaryBase):
    def validateValue(self):
        try:
            float(self._val)
        except Exception:
            return False
        return True
        
    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("square")
        return _keywords

    def convert(self):
        return float(self._val)*float(self._val)

    def getInfo(self):
        return ("Returns the square of the given number \nKeywords: "+ str(self.keywords()))
        

    