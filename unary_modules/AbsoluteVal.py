from .. import UnaryBase

class Inverse(UnaryBase.UnaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def getKeywords(self):
        keywords = ("abs", "absolute")
        return keywords

    def convert(self):
        if self.validateValue():
            return abs(self._val)
        else:
            raise Exception