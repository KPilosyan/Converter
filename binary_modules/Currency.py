from BinaryBase import BinaryBase

import requests 
import json


class Currency(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        url = 'https://api.exchangeratesapi.io/latest'
        r = requests.get(url, params={'base':'USD'})
        __keys = json.loads(r.text)['rates']
        __keys =  {k.lower(): v for k, v in __keys.items()}
        return __keys
       
    def convert(self):
        return int(self._val)*self.getKeys()[self.to]/self.getKeys()[self.fr]
        
