from flask import Flask, request, jsonify
import numpy as np
from DominantColor import DominantColor

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if 'image' not in request.files:
        return jsonify(message="Error")

    f = request.files['image']
    f = np.fromstring(f.stream.getvalue(), np.uint8)

    dominant = DominantColor(f).get()

    return jsonify(color=dominant)

@app.route('/upload')
def upload():
    return '''
    <form action="/" method="post" enctype="multipart/form-data">
    <input type="file" name="image" id="image">
    <input type="submit" value="Upload Image" name="submit">
    </form>
    '''
