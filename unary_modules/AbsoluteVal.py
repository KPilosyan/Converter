from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return self.to in self.getKeys()

    def getKeys(self):
        keywords = ("abs", "absolute")
        return keywords

    def convert(self):
        return abs(int(self._val))
    