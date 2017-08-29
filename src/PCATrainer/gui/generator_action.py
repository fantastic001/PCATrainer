
from PCATrainer.gui.dialogs import * 

class GeneratorAction(QAction):

    def __init__(self, parent, description, generator_class, dialog_class):
        super(QAction, self).__init__(description, parent)
        self.generator_class = generator_class 
        self.dialog_class = dialog_class 
        self.description = description
        self.triggered.connect(self.callback)
        self.parent = parent

    def setModel(self, model):
        self.model = model

    def callback(self):
        generator = self.generator_class(self.dialog_class(
            "Please select your data source", 
            parent=self.parent
        ))
        self.model.train(generator.getData())
