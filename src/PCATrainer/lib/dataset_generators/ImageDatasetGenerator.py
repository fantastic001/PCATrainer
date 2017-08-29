
from ..dataset_generator import * 

from .. import DataSample

import cv2 
import os 

class ImageDatasetGenerator(DatasetGenerator):

    def getData(self):
        path = self.getParams().get("path", "data/")
        res = [] 
        for label in os.listdir(path):
            for imgname in os.listdir("%s/%s" % (path, label)):
                image = cv2.imread("%s/%s/%s" % (path, label, imgname))
                dst = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                res.append(ImageSample(dst, label))
        return res
