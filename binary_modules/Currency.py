from BinaryBase import BinaryBase

import requests 
import json


class Currency(BinaryBase):
    #def __init__(self):
    #    super(MetricBase, self).__init__()

    def validateValue(self):
        return self._val.isdigit()

    def getKeys(self):
        url = 'https://api.exchangeratesapi.io/latest'
        r = requests.get(url, params={'base':'USD'})
        __metrics = json.loads(r.text)['rates']
        return __metrics

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())
        
    def convert(self):
        return self._val*self.getKeys()[self.to]/self.getKeys()[self.fr]

    # def get_converter_class():
    #     return Currency()

