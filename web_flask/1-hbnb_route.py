#!/usr/bin/python3
""" Script will start a flask web application"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strick_slashes=False)
def hello_hbnb():
    """ Prints a message when / is called """
    return 'Hello HBNB!'

@app.route('/hbnb', strick_slashes=False)
def hbnb():
    """ Prints a message when / is called """
    return 'HBNB' 

if __name__ == "__main__":
    """ Main function """
    app.run(host='0.0.0.0', port=5000)
