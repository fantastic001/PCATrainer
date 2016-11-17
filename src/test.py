from lib import * 

m = PCAModel()

m.train([{"label": "a", "sample": [1, 2, 3]}, {"label": "b", "sample": [5, 5, 5]}])

