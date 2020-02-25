from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return True  #Doesn't matter digit or string 
        
    def validateKeywords(self):
        return self.to in self.keywords()

    def keywords(self):
        _keywords = ("inv", "inverse")
        return _keywords

    def convert(self):        
        try:
            if float(self._val) and self._val != 0:
                return 1/float(self._val)  
        except:
            return self._val[::-1]           
        
    def getInfo(self):
        return ("In case input value is digit, returns the inverse of the number"+
        " \nIn case input value is string, returns the letters of the words backwards"+" \nKeywords: "+ str(self.keywords()))
        

    