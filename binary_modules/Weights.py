from .. import MetricBase

class Weights(MetricBase.MetricBase):
    def getMetrics(self):
        __metrics = {'mg':0.001, 'g':1, 'kg':1000, 'ton':1000000, 'lbs':453.59237}
        return __metrics

    def convert(self):
        return self._val*self.getMetrics()[self.fr]/self.getMetrics()[self.to]

    