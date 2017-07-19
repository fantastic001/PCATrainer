


from .VectorListWidget import * 

from .VectorListWidget import * 
from .LabeledVectorListWidget import * 

import json

from gui.dialogs import * 
from lib.dataset_generators import * 

from .generator_action import * 

class MainWindow(QWidget):
    

    def __init__(self, model):
        super(MainWindow, self).__init__()
        
        self.actions = [
            GeneratorAction(self, "Load data from JSON file", JSONDatasetGenerator, QtSelectFileDialog),
            GeneratorAction(self, "Load data from directory structure", DirectoryDatasetGenerator, QtSelectDirectoryDialog)
        ]

        self.ew = VectorListWidget()
        self.tw = LabeledVectorListWidget()
        
        self.model = model
        self.model.connect("trained", self.trained)
        btn_train = QPushButton("Train model")
        btn_save = QPushButton("Save this model")
        btn_save.clicked.connect(self.save)
        btn_restore = QPushButton("Restore saved model")
        btn_restore.clicked.connect(self.restore)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Eigenvectors"))
        layout.addWidget(self.ew)
        layout.addWidget(QLabel("Training data"))
        layout.addWidget(self.tw)
        layout.addWidget(btn_train)
        layout.addWidget(btn_save)
        layout.addWidget(btn_restore)
        self.setLayout(layout)

        menu = QMenu()

        for action in self.actions:
            action.setModel(self.model)
            menu.addAction(action)
        btn_train.setMenu(menu)

        self.repaint()

    def trained(self, **kwargs):
        self.ew.update(kwargs["eigenvectors"])
        self.tw.update(kwargs["data"])

    def save(self):
        filename, other = QFileDialog.getSaveFileName(self, "Select Location to save model")
        self.model.save(filename)

    def restore(self):
        filename, other = QFileDialog.getOpenFileName(self, "Select JSON file with description of the model")
        self.model.restore(filename)
