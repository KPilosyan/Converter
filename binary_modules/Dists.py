from BinaryBase import BinaryBase

class Dists(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        __metrics = {'mm':0.001, 'cm':0.01, 'm':1, 'km':1000}
        return __metrics

    def convert(self):
        return self._val*self.getKeys()[self.fr]/self.getKeys()[self.to]
        