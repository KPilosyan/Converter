from BinaryBase import BinaryBase

class Volumes(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        _keys = {'ml':0.000001, 'l':0.001, 'm3':1, 'km3':1000000000}
        return _keys
        
    def convert(self):
        return int(self._val)*self.getKeys()[self.fr]/self.getKeys()[self.to]