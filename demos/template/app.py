from flask import Flask,render_template,Markup,flash,redirect,url_for

app = Flask(__name__)
user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/watchlist2')
def watchlist():
    return render_template('watchlist2.html',user=user,movies=movies)

@app.route('/')
def index():
    #return render_template('index.html')
    return render_template('index.html')

@app.context_processor
def inject_foo():
    foo = 'I am foo'
    return dict(foo=foo) #等同于return{'foo':foo}


@app.route('/hello')
def hello():
    text = Markup('<h1> Hello,flask！</h1>')
    return render_template('index.html',text=text)

@app.route('/test')
def test():
    return render_template('base.html')


#注册自定义过滤器
from flask import  Markup
@app.template_filter()
def musical(s):
    return s + Markup('&#9835;')

#自定义全局函数
@app.template_global()
def bar():
    return 'I am bar.'

#自定义测试器
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False

#使用flash()函数闪现消息
app.secret_key = 'secret string'
@app.route('/flash')
def just_flash():
    flash('I am flash,who is looking for me?')
    return redirect(url_for('index'))

#404错误处理器
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'),404
