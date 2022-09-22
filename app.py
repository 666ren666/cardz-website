from flask import Flask, request, render_template
from flask.blueprints import Blueprint

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main_page.html')


app.run(debug=True)