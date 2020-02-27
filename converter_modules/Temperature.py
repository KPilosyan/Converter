from Base import Base

class Temperature(Base):
    def validateValue(self):
        try:
            float(self._val)
        except Exception:
            return False
        return True

    def validateKeywords(self):
        return (self.fr in self.keywords() and self.to in self.keywords())

    def keywords(self):
        _keywords = ("c","k","f", "celsus", "kelvin", "fahrenheit")
        return _keywords

    def convert(self):
        if self.fr in ("f", "fahrenheit") and self.to in ("k", "kelvin"):
            res = (float(self._val) - 32)*5/9 + 273.15
            if res < 0:
                return (str(res) +  "\nWarning: Kelvin can't be negative")
            return res
        elif self.fr in ("k", "kelvin") and self.to in ("f", "fahrenheit"):
            res = (float(self._val) - 273.15)*9/5 + 32
            if float(self._val) < 0:               
                return (str(res) +  "\nWarning: Kelvin can't be negative")
            return res
        elif self.fr in ("c", "celsus") and self.to in ("k", "kelvin"):
            res = float(self._val) + 273.15
            if res < 0:
                return (str(res) +  "\nWarning: Kelvin can't be negative")
            return res
        elif self.fr in ("k", "kelvin") and self.to in ("c", "celsus"):
            res = float(self._val) - 273.15  
            if float(self._val) < 0:
                return (str(res) +  "\nWarning: Kelvin can't be negative")
            return res              
        elif self.fr in ("c", "celsus") and self.to in ("f", "fahrenheit"):
            return (float(self._val)*9/5) + 32
        elif self.fr in ("f", "fahrenheit") and self.to in ("c", "celsus"):
            return (float(self._val) - 32)*5/9
        elif self.fr == self.to:
            if float(self._val) < 0 and self.fr in ("k", "kelvin"):
                return (str(self._val) + "\nWarning: Kelvin can't be negative")
            return float(self._val)

    def getInfo(self):
        return ("Converts temperature measuring metrics \nKeywords: "+ str(self.keywords()))
        



 