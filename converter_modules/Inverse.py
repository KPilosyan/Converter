from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return float(self._val) or str(self._val)
        
    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("inv", "inverse")
        return _keywords

    def convert(self):        
        # if float(self._val) and self._val != 0:
        #     return 1/float(self._val)
        if str(self._val):
            return self._val[::-1]   
        
    def getInfo(self):
        return ("Returns the inverse of the given number \nKeywords: "+ str(self.keywords()))
        

    