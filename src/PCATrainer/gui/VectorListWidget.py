

from PyQt5.QtWidgets import * 

class VectorListWidget(QWidget):
    
    def __init__(self):
        super(VectorListWidget, self).__init__()
        layout = QVBoxLayout()
        self.label = QLabel("")
        layout.addWidget(self.label)
        self.items = QListWidget() 
        layout.addWidget(self.items)
        self.setLayout(layout)




    def update(self, vectors):
        self.label.setText("Count: " + str(len(vectors)))
        self.items.clear()
        for v in vectors:
            name = "[ "
            for e in v:
                name += str(e) + " "
            name += "]"
            self.items.addItem(name)
