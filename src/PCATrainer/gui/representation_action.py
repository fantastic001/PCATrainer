
from PCATrainer.gui.dialogs import * 

class RepresentationAction(QAction):

    def __init__(self, parent, description, representation, model, data):
        super(QAction, self).__init__(description, parent)
        self.representation = representation
        self.description = description
        self.triggered.connect(self.callback)
        self.parent = parent
        self.model = model 
        self.data = data 

    def callback(self):
        self.representation.show(self.model, self.data)
