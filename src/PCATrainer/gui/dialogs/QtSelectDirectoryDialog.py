
from PCATrainer.lib import Dialog 


from PyQt5.QtWidgets import * 
class QtSelectDirectoryDialog(Dialog):
    
    def show(self):
        d = QFileDialog.getExistingDirectory(self.getParent(), self.getMessage())
        self.input = {"path": d}

    def getInput(self):
        return self.input
