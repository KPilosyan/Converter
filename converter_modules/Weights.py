from Base import Base

class Weights(Base):
    _metrics = {'mg':0.001, 'g':1, 'kg':1000, 'ton':1000000, 'lbs':453.59237}
    
    def validateValue(self):
        try:
            float(self._val)
        except Exception:
            return False
        return True

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        _keywords = tuple(self._metrics.keys())
        return _keywords

    def convert(self):
        return float(self._val)*self._metrics[self.fr]/self._metrics[self.to]

    def getInfo(self):
        return("Converts weight measurement units \nKeywords: "+ str(self.keywords()))

    