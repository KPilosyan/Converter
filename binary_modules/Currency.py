from BinaryBase import BinaryBase

import requests 
import json


class Currency(BinaryBase):
    def validateValue(self):
        return self._val.isdigit()

    def validateKeys(self):
        return (self.fr in self.getKeys() and self.to in self.getKeys())

    def getKeys(self):
        url = 'https://api.exchangeratesapi.io/latest'
        r = requests.get(url, params={'base':'USD'})
        __metrics = json.loads(r.text)['rates']
        return __metrics
       
    def convert(self):
        return self._val*self.getKeys()[self.to]/self.getKeys()[self.fr]
        
    # def get_class_name(self):
    #     return __class__.__name__
  
