import os

from flask import Flask, render_template, request, jsonify
#from werkzeug import secure_filename

import pandas as pd

from clipr import Profile

app = Flask(__name__)


@app.route('/upload')
def upload():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        idfield = request.form['idfield']
        #f.save(secure_filename(f.filename))
        filepath = os.path.join('uploads', f.filename)
        f.save(filepath)
        data = pd.read_csv(filepath, delimiter=delim(request.form['delimeter']))
        profile = Profile(data=data)
        output = profile.generate_profile()
        return jsonify(output)

def delim(x):
    return {
        '0': ',',
        '1': '\t'
    }.get(x, '\t') 

if __name__ == '__main__':
    app.run(debug=True)
