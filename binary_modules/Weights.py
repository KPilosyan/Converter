from BinaryBase import BinaryBase

class Weights(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getMetrics(self):
        __metrics = {'mg':0.001, 'g':1, 'kg':1000, 'ton':1000000, 'lbs':453.59237}
        return __metrics

    def convert(self):
        return self._val*self.getKeys()[self.fr]/self.getKeys()[self.to]

    