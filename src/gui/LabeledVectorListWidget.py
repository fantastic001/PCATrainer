

from PyQt5.QtWidgets import * 

class LabeledVectorListWidget(QWidget):
    
    def __init__(self):
        """
        data: list of dictionaries with fields sample and label 
        """
        super(LabeledVectorListWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(QLabel(self.label))
        self.items = QListWidget() 
        layout.addWidget(self.items)
        self.setLayout(layout)

    def update(self, data):
        self.label.setText("Count: " + str(len(data)))
        self.items.clear()
        for d in data:
            v = d["sample"]
            label = d["label"]
            name = "[ "
            for e in v:
                name += str(e) + " "
            name += "] " + label
            self.items.addItem(name)
