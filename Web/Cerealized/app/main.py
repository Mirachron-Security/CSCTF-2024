#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from flask import Flask, render_template, request, make_response, redirect, send_file
import random  # Import the random module
import os
import pickle
import base64

template_dir = os.path.dirname(__file__)
print(f"template_dir: {template_dir}")

app = Flask(__name__,template_folder=template_dir)

flag = os.environ.get('FLAG')

@app.route('/pickle.jpg')
def img():
    return send_file('pickle.jpg')

@app.route('/')
def pickling():
    contents = request.cookies.get('contents')
    if contents:
        items = pickle.loads(base64.b64decode(contents))
    else:
        items = []
    return render_template('index.html', items=items, random=random)  

@app.route('/add', methods=['POST'])
def add():
    contents = request.cookies.get('contents')
    if contents:
        items = pickle.loads(base64.b64decode(contents))
    else:
        items = []
    items.append(request.form['item'])
    response = make_response(redirect('/'))
    response.set_cookie('contents', base64.b64encode(pickle.dumps(items)))
    return response

@app.errorhandler(Exception)
def handle_error(error_name):
    return render_template('error.html', message=error_name), 500

if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=9999)
