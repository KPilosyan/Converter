from BinaryBase import BinaryBase

class Times(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        __metrics = {'msec': 1/60000, 'sec':1/60, 'min':1, 'hour':60, 'day':1440, 'week':10080, 'month':43800, 'year':525600}
        return __metrics

    def convert(self):
        return int(self._val)*self.getKeys()[self.fr]/self.getKeys()[self.to]