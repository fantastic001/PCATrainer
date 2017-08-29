
from .data_sample import * 

class ImageSample(DataSample):
    
    def __init__(self, matrix, label):
        h,w = matrix.shape 
        super(DataSample, self).__init__(matrix.reshape(w*h), label)
        self.width = w 
        self.height = h 

    def getWidt(self):
        return self.width

    def getHeight(self):
        return self.height
