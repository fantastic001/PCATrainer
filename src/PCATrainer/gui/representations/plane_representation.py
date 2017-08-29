
from PCATrainer.lib import DataRepresentation

import matplotlib.pyplot as plt 

class PlaneRepresentation(DataRepresentation):
    
    def setup(self, **params):
        pass

    def show(self, model, data):
        points = [] 
        for d in data:
            points.append(model.project(d)[:2])
        x = [] 
        y = [] 
        for p in points:
            x.append(p[0])
            y.append(p[1])
        plt.plot(x,y,"o")
        plt.title("Data projected to 2D plane")
        plt.show()
