#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '98765432123456789'

@app.route('/')
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False

    if session['logged_in']:
        return '<h1 style=text-align:center>You are logged in!</h1>'
    else:
        return '<h1 style=text-align:center>Access Denied</h1><div style="text-align: center;"><img src="https://i.imgur.com/Xka7TuR.png" alt="secret key flask" width="1000"></div> ', 403

if __name__ == '__main__':
    app.run("0.0.0.0", port=9999)