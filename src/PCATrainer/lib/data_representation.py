
class DataRepresentation(object):

    def __init__(self, **params):
        self.setup(**params)

    def setup(self, **params):
        pass

    def show(self, model, data):
        """
        model: PCAModel object 
        data: list of DataSample objects
        """
        pass
