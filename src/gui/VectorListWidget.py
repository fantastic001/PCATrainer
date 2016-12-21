

from PyQt5.QtWidgets import * 

class VectorListWidget(QWidget):
    
    def __init__(self, vectors):
        super(VectorListWidget, self).__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Count: " + str(len(vectors))))
        items = QListWidget() 

        for v in vectors:
            name = "[ "
            for e in v:
                name += str(e) + " "
            name += "]"
            items.addItem(name)
        layout.addWidget(items)
        self.setLayout(layout)

