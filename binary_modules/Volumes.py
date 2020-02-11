from BinaryBase import BinaryBase

class Volumes(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        __metrics = {'ml':0.000001, 'l':0.001, 'm3':1, 'km3':1000000000}
        return __metrics
        
    def convert(self):
        return int(self._val)*self.getKeys()[self.fr]/self.getKeys()[self.to]