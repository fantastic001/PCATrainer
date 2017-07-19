

from .. import DatasetGenerator 

import json 

class JSONDatasetGenerator(DatasetGenerator):

    def getData(self):
        params = self.getParams()
        f = open(params.get("filename", "data.json"))
        source = f.read()
        data = json.loads(source)["data"]
        return data
