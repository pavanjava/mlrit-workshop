from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def default_message():
    return 'Hello MLRIT, welcome to the cloud explore workshop'


@app.route('/message')
def message_with_param():
    return 'data passed to server: ' + request.args.get('data')
