from BinaryBase import BinaryBase

class Weights(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        _keys = {'mg':0.001, 'g':1, 'kg':1000, 'ton':1000000, 'lbs':453.59237}
        return _keys

    def convert(self):
        return int(self._val)*self.getKeys()[self.fr]/self.getKeys()[self.to]

    