
from .. import DatasetGenerator 

from .. import DataSample

import os 

class DirectoryDatasetGenerator(DatasetGenerator):

    def getData(self):
        path = self.getParams().get("path", "data/")
        res = []
        for label in os.listdir(path):
            for sample_name in os.listdir("%s/%s/" % (path, label)):
                f = open("%s/%s/%s" % (path, label, sample_name))
                sample = [] 
                for line in f:
                    sample.append(float(line))
                res.append(DataSample(sample, label))
        return res
