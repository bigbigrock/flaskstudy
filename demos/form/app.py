from flask import Flask,render_template,request,redirect,url_for,flash,session,send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from forms import LoginForm,UploadForm,MultiUploadForm,RichTextForm
import os
import uuid
from flask_wtf.csrf import validate_csrf
from wtforms import ValidationError

from flask_ckeditor import CKEditor

app = Flask(__name__)
# app_ctx = app.app_context()
# app_ctx.push()
app.secret_key = "secret string"
# @app.route('/bootstrap')
# def basic():
#     form = LoginForm()
#     return render_template('bootstrap.html',form=form)

@app.route('/',methods=['GET','POST'])
def index():
    return  render_template('index.html')

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

# #实例化表单类
# @app.route('/upload',methods=['GET','POST'])
# def upload():
#     form = UploadForm()
#     ...
#     return render_template('upload.html',form=form)

#处理上传文件
app.config['UPLOAD_PATH'] = os.path.join(app.root_path,'uploads')
@app.route('/upload',methods = ['GET','POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = random_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_PATH'],filename))
        flash('Upload sucess')
        session['filenames'] = [filename]
        return redirect(url_for('show_image'))
    return render_template('upload.html',form=form)

#重命名文件
def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_name = uuid.uuid4().hex + ext
    return new_name

@app.route('/uploads/<path:filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOAD_PATH'],filename)

@app.route('/uploaded-images')
def show_images():
    return render_template('uploded.html')

#处理多文件上传
@app.route('/multi-upload',methods=['GET','POST'])
def multi_upload():
    form = MultiUploadForm()
    if request.method == "POST":
        filenames = []
        #验证CSRF令牌
        try:
            validate_csrf(form.csrf_token.data)
        except ValidationError:
            flash('CSRF token error')
            return redirect(url_for('multi_upload'))
        #检查文件是否存在
        if 'photo' not in request.files:
            flash('This field is required')
            return redirect(url_for('multi_upload'))


        for f in request.files.getlist('photo'):
            #检查文件类型
            if f and allowed_file(f.filename):
                filename = random_filename(f.filename)
                f.save(os.path.join(
                    app.config['UPLOAD_PATH'],filename
                ))
                filenames.append(filename)
            else:
                flash('Invalid file type')
                return redirect(url_for('multi_upload'))
        flash('Upload sucess')
        session['filenames']=filename
        return redirect(url_for('show_images'))
    return render_template('upload.html',form=form)

#验证文件类型
app.config['ALLOWED_EXTENSIONS']=['png','jpg','jpeg','gif']
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

#富文本
app.config['CKEDITOR_SERVE_LOCAL']=True
ckeditor = CKEditor(app)
@app.route('/ckeditor',methods=['GET','POST'])
def integrate_ckeditor():
    form = RichTextForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        flash('Your post is published')
        return render_template('post.html',title=title,body=body)
    return render_template('ckeditor.html',form=form)


