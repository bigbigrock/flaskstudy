from flask import Flask,url_for
import click
app = Flask(__name__)

# @app.route('/')
# def index():
#     return "hello flask"

# @app.route('/hello/<name>')
# def greet(name):
#     return url_for('greet',name='jack',_external=True)

@app.cli.command('hi')
def helloo():
    """just say hello"""
    click.echo('hello,human!')
