from BinaryBase import BinaryBase

class Temperature(BinaryBase):
    def validateValue(self):
        return float(self._val)

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        _keywords = ("c","k","f", "celsus", "kelvin", "fahrenheit")
        return _keywords

    def convert(self):
        if self.fr in ("f", "fahrenheit") and self.to in ("k", "kelvin"):
            return (int(self._val) - 32)*5/9 + 273.15
        elif self.fr in ("k", "kelvin") and self.to in ("f", "fahrenheit"):
            return (int(self._val) - 273.15)*9/5 + 32
        elif self.fr in ("c", "celsus") and self.to in ("k", "kelvin"):
            return int(self._val) + 273.15
        elif self.fr in ("k", "kelvin") and self.to in ("c", "celsus"):
            return int(self._val) - 273.15
        elif self.fr in ("c", "celsus") and self.to in ("f", "fahrenheit"):
            return (int(self._val)*9/5) + 32
        elif self.fr in ("f", "fahrenheit") and self.to in ("c", "celsus"):
            return (int(self._val) - 32)*5/9
        elif self.fr == self.to:
            return int(self._val)

    def getInfo(self):
        return ("Converts temperature measuring metrics \nKeywords: "+ str(self.keywords()))
        



 