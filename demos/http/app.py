from flask import Flask,request,redirect,url_for,abort,make_response,jsonify
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

#模拟管理后台
# from flask import session,abort
# @app.route('/admin')
# def admin():
#     if 'logged_in' not in session:
#         abort(403)
#     return 'Welcome to admin page'

#登出用户
# from flask import session
# @app.route('/logout')
# def logout():
#     if 'logged_in' in session:
#         session.pop('logged_in')
#     return redirect(url_for('hello'))


# @app.route('/foo')
# def foo():
#     return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>'%url_for('do_something',next=request.full_path)

# @app.route('/bar')
# def bar():
#     return '<h1>Foo page</h1><a href="%s">Do something and redirect</a>'%url_for('do_something',next=request.full_path)

# @app.route('/do_something_and_redirect')
# def do_something():
#     # do something
#     # return redirect(request.referer or url_for('hello'))
#     #  return redirect(request.args.get('next',url_for('hello')))
#     return redirect_back()
#
# def redirect_back(default='hello',**kwars):
#     for target in request.args.get('next'),request.referer:
#         if not target:
#             continue
#         if is_safe_url(target):
#             return redirect(target)
#     return redirect(url_for(default,**kwars))
#
# #验证URL安全性
# from urllib.parse import urlparse,urljoin
# from flask import request
# def is_safe_url(target):#接收目标URL作为参数
#     ref_url = urlparse(request.host_url)#request.host_url获取程序内的主机URL
#     test_url = urlparse(urljoin(request.hosturl,target))#urljoin将目标URL转换为绝对URL。
#     return test_url.scheme in('http','https')and ref_url.netloc == test_url.netloc#对目标URL的URL模式和主机地址进行验证。

#纯文本或局部HTML模板

from jinja2.utils import generate_lorem_ipsum
@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=5)
    return """
    <h1>A very long post</h1>
    <div class="body">%s</div>
    <button id="load">Load More</button>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script type="text/javascript">
    $(function(){
    $('#load').click(function(){//$('#load')被称为选择器，括号中传入目标元素的id、class或是其他属性来定位到对应的元素
    $.ajax({
    url:'/more',//目标URL
    type:'get',//请求方法
    sucess:function(data){//返回2xx响应后触发的回调函数
    $('.body').append(data);//将返回的响应插入到页面中
    }
    })
    })
    })
    </script>"""%post_body

@app.route('/more')
def load_post():
    return generate_lorem_ipsum(n=1)

