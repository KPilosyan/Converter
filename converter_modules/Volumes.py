from BinaryBase import BinaryBase

class Volumes(BinaryBase):
    _metrics = {'ml':0.000001, 'l':0.001, 'm3':1, 'km3':1000000000}

    def validateValue(self):
        return float(self._val)

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        _keywords = self._metrics.keys()
        return _keywords
        
    def convert(self):
        return int(self._val)*self._metrics[self.fr]/self._metrics[self.to]

    def getInfo(self):
        return 