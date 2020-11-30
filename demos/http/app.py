from flask import Flask,request,redirect,url_for,abort,make_response,jsonify,session
import os

app = Flask(__name__)
# @app.route('/hello',methods=['GET','POST'])
# def hello1():
#     name = request.args.get('name','Flask') #获取查询参数name的值
#     # name = request.args.get('name') #获取查询参数name的值
#     return '<h1>hello,%s!</h1>'%name #插入到返回值中


# @app.route('/goback/<int:year>')
# def go_back(year):
#     return '<p>Welcome to %d!</p>'%(2018 - year)


# @app.route('/colors/<any(blue,white,red):color>')
# def three_colors(color):
#     return '<p>Love is patient and kind.Love is not jealous or boastful or proud or rude.</p>'
#
# colors = ['blue','white','red']
#
# @app.route('/colors/<any(%s):color>'%str(colors)[1:-1])
# def three_colors(color):
#     return '<p>Love is patient and kind.Love is not jealous or boastful or proud or rude.</p>'

# @app.before_request
# def do_something():
#     pass  #这里的代码会在每个请求处理前执行

# @app.route('/hello')
# def hello():
#     ...
#     return '',302,{'Location':'http://www.example.com'}

#重定向
# @app.route('/hello')
# def hello():
#     return redirect('http://www.example.com')

# #重定向到其他视图函数
# @app.route('/hi')
# def hi():
#     ...
#     return redirect(url_for('hello'))  #重定向到hello
#
# @app.route('/404')
# def not_found():
#     abort(404)


# @app.route('/foo')
# def foo():
#     response = make_response('hello,world')
#     response.mimetype = 'text/plain'
#     return response

# @app.route('/foo')
# def foo():
#     return jsonify(name='grey li',gender='male')
#
# @app.route('/set/<name>')
# def set_cookie(name):
#     response = make_response(redirect(url_for('hello')))
#     response.set_cookie('name',name)
#     return response

app.secret_key = os.getenv('SECRET_KEY','secret string')

@app.route('/login')
def login():
    session['logged_in'] = True #写入session
    return redirect(url_for('hello'))

from flask import request,session
@app.route('/')
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Human')
        response = '<h1>Hello,%s!</h1>'%name
    #根据用户认证状态返回不同的内容
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response





