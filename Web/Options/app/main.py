#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

from flask import Flask, redirect, send_file, request, make_response
from werkzeug.exceptions import HTTPException, MethodNotAllowed
import os

app = Flask(__name__)

FLAG = os.environ.get('FLAG')

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def start():
        return redirect('/one')

    @app.route('/one', methods=['GET'])
    def route_one():
        index_content = send_file_or_redirect('index.html', '/anotherone')
        response = make_response(index_content)
        response.headers['Location'] = '/anotherone'
        response.status_code = 302
        return response

    @app.route('/anotherone', methods=['GET'])
    def route_anotherone():
        return redirect('/flag')

    @app.route('/flag', methods=['GET'])
    def show_flag():
        return 'You want the flag? You just started and already lost track of where you are. Such a fool...'

    @app.route('/hint', methods=['GET'])
    def hint():
        return 'Don\'t tell anyone, but I think I saw someone posted up at /userapp.'

    @app.route('/userapp', methods=['POST'])
    def userapp():
        return 'Hidden Linux files have a period prepended. Do you think I hid the hidden file? hidden hidden'

    @app.route('/.hidden', methods=['PUT'])
    def get_flag():
        return f'You saw so many options! You deserve a flag: {FLAG}!'

    # Handle non-existent routes, providing a clue for the next step
    @app.route('/<path:invalid_path>', methods=['GET', 'PUT'])
    def nowhere(invalid_path):
        return f'This path leads nowhere. What other *options* do you have?'

    @app.errorhandler(MethodNotAllowed)
    def handle_method_not_allowed(e):
        allowed_methods = ', '.join(e.valid_methods) if e.valid_methods else 'None'
        return f'This method is not allowed for the requested URL. \nAllowed methods: {allowed_methods}', 405


    def send_file_or_redirect(file_path, redirect_path):
        if 'redirect' in request.args:
            return redirect(redirect_path)
        return send_file(file_path)

    return app

if __name__ == '__main__':
    create_app().run(threaded=True, host="0.0.0.0", port=9999)
