from .. import UnaryBase

class Inverse(UnaryBase.UnaryBase):
    def validateValue(self):
        return self._val.isdigit()
        
    def getKeywords(self):
        keywords = ("inv", "inverse")
        return keywords

    def convert(self):
        if self.validateValue():
            return 1/self._val
        else:
            raise Exception


    