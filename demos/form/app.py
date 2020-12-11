from flask import Flask,render_template,request,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from forms import LoginForm


app = Flask(__name__)
# app_ctx = app.app_context()
# app_ctx.push()
app.secret_key = "secret string"
# @app.route('/bootstrap')
# def basic():
#     form = LoginForm()
#     return render_template('bootstrap.html',form=form)


@app.route('/basic',methods=['get','post'])
def basic():
    form = LoginForm()#GET+POST
    if form.validate_on_submit():#提交了表单并通过了验证
        #if request.method == 'POST' and form.validate():
        username = form.username.data
        flash('Welcome home,%s!'%username)
        return redirect(url_for('basic'))
    return render_template('basic.html',form=form)#处理GET请求

#设置内置错误消息语言为中文
app.config['WTF_I18N_ENABLED']=False
class MyBaseForm(FlaskForm):
    class Meta:
        locales=['zh']
class HelloForm(MyBaseForm):
    name = StringField('name',validators=[DataRequired()])
    submit = SubmitField