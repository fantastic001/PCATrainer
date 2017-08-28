

from .. import DatasetGenerator 

from .. import DataSample

import json 

class JSONDatasetGenerator(DatasetGenerator):

    def getData(self):
        params = self.getParams()
        f = open(params.get("filename", "data.json"))
        source = f.read()
        data = json.loads(source)["data"]
        res = [] 
        for entry in data:
            res.append(DataSample.fromDict(entry))
        return res
