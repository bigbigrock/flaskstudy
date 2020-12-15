from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField,MultipleFileField
from wtforms.validators import DataRequired,Length,ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed

from flask_ckeditor import CKEditorField

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

#行内验证器
class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number')
    submit = SubmitField()
    def validate_answer(form,field):
        if field.data != 42:
            raise ValidationError("Must be 42")
#全局验证器
def is_42(form,field):
    if field.data !=42:
        raise ValidationError('Must be 42')

class FortyTwoForm(FlaskForm):
        answer = IntegerField('The Number',validators=[is_42])
        submit = SubmitField()

#工厂函数形式的全局验证器示例
def is_42(message=None):
    if message is None:
        message = 'Must be 42'
    def _is_42(form,field):
        if field.data != 42:
            raise ValidationError(message)
    return _is_42

class FortyTwoForm(FlaskForm):
    answer = IntegerField('The Number',validators=[is_42()])
    submit = SubmitField

#创建上传表单
class UploadForm(FlaskForm):
    photo = FileField('Upload Image',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png','gif'])])
    submit = SubmitField()

#多文件上传
class MultiUploadForm(FlaskForm):
    photo = MultipleFileField('Upload Image',validators=[DataRequired()])
    submit = SubmitField()

#文章表单
class RichTextForm(FlaskForm):
    title = StringField('title',validators=[DataRequired(),Length(1,50)])
    body = CKEditorField('Body',validators=[DataRequired()])
    submit = SubmitField('Publish')
