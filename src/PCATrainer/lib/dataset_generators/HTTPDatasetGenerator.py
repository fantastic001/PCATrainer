

from .. import DatasetGenerator 

from .. import DataSample

import requests

import os 

class HTTPDatasetGenerator(DatasetGenerator):
    """
    Params: 
    url: url to data over HTTP
    """

    def getData(self):
        url = self.getParams().get("url", "http://localhost")
        res = []
        data = requests.get(url).json()
        for d in data:
            res.append(DataSample.fromDict(d))
        return res
