

from sklearn.decomposition import PCA
import numpy as np 
from random import shuffle
import json

class NoSignalException(Exception):
    pass

class NotTrainedException(Exception):
    pass

class PCAModel(object):

    def __init__(self):
        self.model = None
        self.events = {
            "trained": self.nothing,
            "validated": self.nothing,
            "classified": self.nothing
        }

    def train(self, data):
        """
        data: list of dicts with 'label' and 'sample'
        """
        self.model = PCA(n_components=None)
        self.data = data
        n_features = len(data[0]["sample"])
        n_samples = len(data)
        self.training = np.zeros([n_samples, n_features])
        for i in range(n_samples):
            for j in range(n_features):
                self.training[i,j] = data[i]["sample"][j]
        self.model.fit(self.training)
        self.events["trained"](eigenvectors=self.model.components_, eigenvalues=[], mean=self.model.mean_, data=data)

    def classify(self, sample):
        """
        Classifies given sample

        Returns: (label, distance)
        """
        if self.model == None:
            raise NotTrainedException()
        dt = self.project(np.array(self.data[0]["sample"])) - self.project(np.array(sample))
        mind = np.sqrt(dt.dot(dt))
        res = self.data[0]["label"]
        for t in self.data:
            dt = self.project(np.array(t["sample"])) - self.project(np.array(sample))
            d = np.sqrt(dt.dot(dt))
            if d < mind:
                mind = d
                res = t["label"]
        return (res, mind)
            

    def validate(self, validation_data, iters):
        """
        Does cross validation on data 

        iters: number of iterations for cross validation 
        validation_data: list of dicts with keys 'label' and 'sample'
        """
        n = len(validation_data)
        correct = 0;
        k = int(0.1*n)
        for i in range(iters):
            shuffle(self.data)
            self.train(validation_data[:k])
            for test in validation_data[k:]:
                l,d = self.classify(test["sample"])
                if l == test["label"]:
                    correct = correct + 1
        return correct / float(iters * len(validation_data[k:])) 



    def project(self, sample):
        """
        Projects sample - mean into subspace 
        """
        eigens = self.get_eigenvectors()
        res = []
        for e in eigens:
            res.append(e.dot(np.array(sample) - self.get_mean()))
        return np.array(res)

    def get_eigenvectors(self):
        return self.model.components_

    def get_mean(self):
        return self.model.mean_

    def save(self, path):
        eigen = self.get_eigenvectors()
        mean = self.get_mean()
        data = self.data 
        json_eigen = []
        json_mean = [] 
        json_data = []
        for e in eigen:
            curr = []
            for elem in e:
                curr.append(elem)
            json_eigen.append(curr)
        for e in mean:
            json_mean.append(e)
        for d in data:
            t = {}
            t["label"] = d["label"]
            t["sample"] = [] 
            for e in d["sample"]:
                t["sample"].append(e)
            json_data.append(d)
        s = json.dumps({"eigevectors": json_eigen, "mean": json_mean, "data": json_data})
        f = open(path, "w")
        f.write(s)
        f.close()

    def restore(self, path):
        f = open(path)
        data = json.loads(f.read())
        self.train(data["data"])

    def connect(self, event, fun):
        """
        Connect to signal emmited by model 

        Signals can be:

        trained: function gets keyword arguments 'eigenvectors', 'eigenvalues', 'mean' and 'data' where each element is dict {'label', 'sample'}
        validated: function gets keyword argument 'precision', 'accuracy' and 'validation_data' where each element is dict {'label', 'sample'}
        classified: function with keyword argument 'sample' and 'label' 
        """
        if not event in self.events:
            raise NoSignalException()
        else:
            self.events[event] = fun
    
    def nothing(self, **kwargs):
        pass
