

from PyQt5.QtWidgets import * 

class LabeledVectorListWidget(QWidget):
    
    def __init__(self, data):
        """
        data: list of dictionaries with fields sample and label 
        """
        super(LabeledVectorListWidget, self).__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Count: " + str(len(data))))
        items = QListWidget() 

        for d in data:
            v = d["sample"]
            label = d["label"]
            name = "[ "
            for e in v:
                name += str(e) + " "
            name += "] " + label
            items.addItem(name)
        layout.addWidget(items)
        self.setLayout(layout)

