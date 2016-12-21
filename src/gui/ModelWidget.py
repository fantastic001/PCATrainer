


from .VectorListWidget import * 

from .VectorListWidget import * 
from .LabeledVectorListWidget import * 

class ModelWidget(QWidget):
    
    def __init__(self):
        super(ModelWidget, self).__init__()
        self.ew = VectorListWidget()
