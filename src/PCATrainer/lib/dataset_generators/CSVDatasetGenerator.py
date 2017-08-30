

from .. import DatasetGenerator 

from .. import DataSample

import os 

class CSVDatasetGenerator(DatasetGenerator):
    """
    Params: 
    filename: path to CSV file
    """

    def getData(self):
        path = self.getParams().get("filename", "data/")
        res = []
        f = open(path)
        for line in f:
            array = line.split(",")
            label = array[0]
            rest = array[1:]
            sample = [] 
            for r in rest:
                sample.append(float(r))
            res.append(DataSample(sample, label))
        return res
