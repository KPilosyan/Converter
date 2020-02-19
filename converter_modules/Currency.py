from BinaryBase import BinaryBase

import requests 
import json


class Currency(BinaryBase):
    url = 'https://api.exchangeratesapi.io/latest'
    r = requests.get(url, params={'base':'USD'})
    _metrics = json.loads(r.text)['rates']
    _metrics =  {k.lower(): v for k, v in _metrics.items()}

    def validateValue(self):
        return float(self._val)

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        return self._metrics.keys()
       
    def convert(self):
        if self._metrics[self.fr] != 0:
            return int(self._val)*self._metrics[self.to]/self._metrics[self.fr]
        raise Exception("Can't divide by 0")

    def getInfo(self):
        return