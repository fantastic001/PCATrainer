
class DatasetGenerator(object):

    def __init__(self, dialog):
        dialog.show()
        self.params = dialog.getInput()

    def getParams(self):
        return self.params

    def getData(self):
        """
        Returns list of DataSample objects
        """
        pass
