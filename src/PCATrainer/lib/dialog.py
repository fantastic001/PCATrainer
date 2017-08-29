
class Dialog(object):

    def __init__(self, msg, parent=None):
        self.msg = msg
        self.parent = parent

    def getParent(self):
        return self.parent 

    def getMessage(self):
        return self.msg 

    def show(self):
        pass

    def getInput(self):
        pass
