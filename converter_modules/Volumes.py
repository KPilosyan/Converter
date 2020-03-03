from Base import Base

class Volumes(Base):
    _metrics = {'ml':0.000001, 'l':0.001, 'm3':1, 'km3':1000000000}

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
        return ("Converts volume measurement units \nKeywords: "+ str(self.keywords()))