from BinaryBase import BinaryBase

class Inverse(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeys(self):
        return self.to in self.getKeys()

    def getKeys(self):
        keys = ("abs", "absolute")
        return keys

    def convert(self):
        return abs(int(self._val))
    