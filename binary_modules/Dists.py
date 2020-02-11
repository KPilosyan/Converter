from ... import MetricBase

class Dists(MetricBase.MetricBase):
    def getMetrics(self):
        __metrics = {'mm':0.001, 'cm':0.01, 'm':1, 'km':1000}
        return __metrics

    def convert(self):
        return self._val*self.getMetrics()[self.fr]/self.getMetrics()[self.to]