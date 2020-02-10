from .. import MetricBase

class Temperature(MetricBase.MetricBase):
    def getMetrics(self):
        __metrics = {"c": None,"k": None,"f": None}
        return __metrics

    def convert(self):
        if self.fr == "f" and self.to == "k":
            return (self._val - 32)*5/9 + 273.15
        elif self.fr == "k" and self.to == "f":
            return (self._val - 273.15)*9/5 + 32
        elif self.fr == "c" and self.to == "k":
            return self._val + 273.15
        elif self.fr == "k" and self.to == "c":
            return self._val - 273.15
        elif self.fr == "c" and self.to == "f":
            return (self._val*9/5) + 32
        elif self.fr == "f" and self.to == "c":
            return (self._val - 32)*5/9
        elif self.fr == self.to:
            return self._val



 