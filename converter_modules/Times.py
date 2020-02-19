from BinaryBase import BinaryBase

class Times(BinaryBase):
    _metrics = {'msec': 1/60000, 'sec':1/60, 'min':1, 'hour':60, 'day':1440, 'week':10080, 'month':43800, 'year':525600}

    def validateValue(self):
        return float(self._val)
        
    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        _keywords = tuple(self._metrics.keys())
        return _keywords

    def convert(self):
        return float(self._val)*self._metrics[self.fr]/self._metrics[self.to]
    
    def getInfo(self):
        return ("Converts time measurement units \nKeywords: "+ str(self.keywords()))