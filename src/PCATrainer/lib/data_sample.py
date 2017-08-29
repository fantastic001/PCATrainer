
import numpy as np 

class DataSample(object):

    def __init__(self, sample, label=None):
        self.sample = sample
        self.label = label 

    def hasLabel(self):
        return self.label != None

    def getLabel(self):
        return self.label 

    def getSample(self):
        return self.sample

    def toDict(self):
        sample = [] 
        for s in self.sample:
            sample.append(s)
        if self.hasLabel():
            return {
                "label": self.label,
                "sample": sample
            }
        else:
            return {
                "sample": sample,
            }
    
    def fromDict(d):
        if "label" in d:
            return DataSample(np.array(d["sample"]), d["label"])
        else:
            return DataSample(np.array(d["sample"]))
