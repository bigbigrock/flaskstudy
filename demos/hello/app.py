from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def index():
    return '<h1>hello hahah </h1>' \
           '<h1>加油吧<h1>'\
           '<h1>hahahhahaha</h1>'\
           '<p>hdhdhdh</p>'

