


from .VectorListWidget import * 

from .VectorListWidget import * 
from .LabeledVectorListWidget import * 

import json

class MainWindow(QWidget):
    
    def __init__(self, model):
        super(MainWindow, self).__init__()
        self.ew = VectorListWidget()
        self.tw = LabeledVectorListWidget()
        
        self.model = model
        self.model.connect("trained", self.trained)
        btn_train = QPushButton("Train model")
        btn_train.clicked.connect(self.train)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Eigenvectors"))
        layout.addWidget(self.ew)
        layout.addWidget(QLabel("Training data"))
        layout.addWidget(self.tw)
        layout.addWidget(btn_train)
        self.setLayout(layout)
        self.repaint()

    def train(self):
        filename, other = QFileDialog.getOpenFileName(self, "Select JSON file with data")
        f = open(filename)
        source = f.read()
        self.model.train(json.loads(source))
        
    def trained(self, **kwargs):
        self.ew.update(kwargs["eigenvectors"])
        self.tw.update(kwargs["data"])
