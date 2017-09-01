


from .VectorListWidget import * 

from .VectorListWidget import * 
from .LabeledVectorListWidget import * 

import json

from PCATrainer.gui.dialogs import * 
from .representations import * 
from PCATrainer.lib.dataset_generators import * 

from .generator_action import * 
from .representation_action import * 

class MainWindow(QWidget):
    

    def __init__(self, model):
        super(MainWindow, self).__init__()
        
        self.actions = [
            GeneratorAction(self, "Load data from JSON file", JSONDatasetGenerator, QtSelectFileDialog),
            GeneratorAction(self, "Load data from CSV file", CSVDatasetGenerator, QtSelectFileDialog),
            GeneratorAction(self, "Load data over HTTP", HTTPDatasetGenerator, QtHTTPDialog),
            GeneratorAction(self, "Load data from directory structure", DirectoryDatasetGenerator, QtSelectDirectoryDialog),
            GeneratorAction(self, "Load data from directory structure with images", ImageDatasetGenerator, QtSelectDirectoryDialog)
        ]

        self.ew = VectorListWidget()
        self.tw = LabeledVectorListWidget()
        
        self.model = model
        self.model.connect("trained", self.trained)
        btn_train = QPushButton("Train model")
        btn_visualize = QPushButton("Visualize data and model")
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
        layout.addWidget(btn_visualize)
        layout.addWidget(btn_save)
        layout.addWidget(btn_restore)
        self.setLayout(layout)

        menu = QMenu()

        self.representationMenu = QMenu()
        btn_visualize.setMenu(self.representationMenu)

        for action in self.actions:
            action.setModel(self.model)
            menu.addAction(action)
        btn_train.setMenu(menu)

        self.repaint()

    def trained(self, **kwargs):
        self.ew.update(kwargs["eigenvectors"])
        self.tw.update(kwargs["data"])
        data = kwargs["data"]
        
        representations = [
            RepresentationAction(self, "2D projection", PlaneRepresentation(), self.model, data)
        ]
        for representation in representations:
            self.representationMenu.addAction(representation)


    def save(self):
        filename, other = QFileDialog.getSaveFileName(self, "Select Location to save model")
        self.model.save(filename)

    def restore(self):
        filename, other = QFileDialog.getOpenFileName(self, "Select JSON file with description of the model")
        self.model.restore(filename)
