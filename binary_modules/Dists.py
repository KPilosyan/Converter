from BinaryBase import BinaryBase

class Dists(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        _keys = {'mm':0.001, 'cm':0.01, 'm':1, 'km':1000}
        return _keys

    def convert(self):
        return int(self._val)*self.getKeys()[self.fr]/self.getKeys()[self.to]
        