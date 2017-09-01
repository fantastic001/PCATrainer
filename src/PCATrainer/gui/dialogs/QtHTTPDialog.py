
from PCATrainer.lib import Dialog 

from PyQt5.QtWidgets import *

class QtHTTPDialog(Dialog):
    
    def show(self):
        self.url, ok = QInputDialog.getText(self.getParent(), "Enter URL", "Pease enter URL of HTTP spot")

    def getInput(self):
        return {"url": self.url}
