from flask import Flask

import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    a = np.arange(15).reshape(3, 5)
    return "Here is a numpy array: "  + str(a)
