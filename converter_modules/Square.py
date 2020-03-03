from Base import Base

class Square(Base):
    def validateValue(self):
        try:
            float(self._val)
        except Exception:
            return False
        return True
        
    def validateKeywords(self):
        if self.to in self.keywords() and self.fr:
            raise Exception("Square conversion doesn't require argument 'fr'") 
        return self.to in self.keywords()
       

    def keywords(self):
        _keywords = ("square")
        return _keywords

    def convert(self):
        return float(self._val)*float(self._val)

    def getInfo(self):
        return ("Returns the square of the given number \nKeywords: "+ str(self.keywords()))
        

    