from flask import Flask, render_template
from app import app
from models import *

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('default.html')
