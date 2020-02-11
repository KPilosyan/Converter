from .. import MetricBase

class Volumes(MetricBase.MetricBase):
    def getMetrics(self):
        __metrics = {'ml':0.000001, 'l':0.001, 'm3':1, 'km3':1000000000}
        return __metrics
        
    def convert(self):
        return self._val*self.getMetrics()[self.fr]/self.getMetrics()[self.to]