import os
from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

