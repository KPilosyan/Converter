from Base import Base

class Dists(Base):
    _metrics = {'mm':0.001, 'cm':0.01, 'm':1, 'km':1000}

    def validateValue(self):
        try:
            float(self._val)
        except Exception:
            return False
        return True

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        return tuple(self._metrics.keys())

    def convert(self):
        if self._metrics[self.to] != 0:
            return float(self._val)*self._metrics[self.fr]/self._metrics[self.to]
        raise Exception("Can't devide by 0")
        
    def getInfo(self):
        return ("Converts metrics measuring distance \nKeywords: "+ str(self.keywords()))

        

        