from PCATrainer.lib import * 

import json
import numpy as np 
m = PCAModel()


validation_data = [
    {"label": "a", "sample": [1,2,3]},
    {"label": "a", "sample": [1,5,3]},
    {"label": "a", "sample": [1,7,3]},
    {"label": "a", "sample": [1,8,3]},
    {"label": "a", "sample": [1,9,3]},
    {"label": "a", "sample": [1,10,3]},
    {"label": "b", "sample": [10,2,3]},
    {"label": "b", "sample": [10,5,3]},
    {"label": "b", "sample": [10,7,3]},
    {"label": "b", "sample": [10,8,3]},
    {"label": "b", "sample": [10,9,3]},
    {"label": "b", "sample": [10,10,3]},
    {"label": "b", "sample": [10,11,3]},
    {"label": "b", "sample": [10,12,3]},
    {"label": "b", "sample": [10,15,3]},
]

data = [{"label": "a", "sample": [1, 2, 3]}, {"label": "b", "sample": [5, 5, 5]}]

f = open("/home/stefan/train.json", "w")
f.write(json.dumps(data))
f.close()



from PCATrainer.gui import * 
import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

window = MainWindow(m)
window.show()

sys.exit(app.exec_())
