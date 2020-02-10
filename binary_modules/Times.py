from .. import MetricBase

class Times(MetricBase.MetricBase):
    def getMetrics(self):
        __metrics = {'msec': 1/60000, 'sec':1/60, 'min':1, 'hour':60, 'day':1440, 'week':10080, 'month':43800, 'year':525600}
        return __metrics
    def convert(self):
        return self._val*self.getMetrics()[self.fr]/self.getMetrics()[self.to]