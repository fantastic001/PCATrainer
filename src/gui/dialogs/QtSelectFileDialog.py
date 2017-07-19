
from lib import Dialog 

from PyQt5.QtWidgets import * 

class QtSelectFileDialog(Dialog):
    
    def show(self):
        filename, other = QFileDialog.getOpenFileName(self.getParent(), self.getMessage())
        self.input = {"filename": filename}

    def getInput(self):
        return self.input
