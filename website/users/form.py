from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from website.models import User

class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱', 
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('信箱',
                            validators =[DataRequired(), Email()])
    password = PasswordField('密碼', validators=[DataRequired()])
    confirm_password = PasswordField('確認密碼',
                            validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('註冊')

    # 錯誤訊息
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('用戶名已經有人使用囉')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('信箱已經有人使用囉')

class LoginForm(FlaskForm):
    email = StringField('信箱',
                            validators=[DataRequired(),Email()])
    password = PasswordField('密碼',validators=[DataRequired()])
    remember = BooleanField('記得帳號')
    submit = SubmitField('登入')

class UpdateAccountForm(FlaskForm):
    username = StringField('使用者名稱', 
                            validators = [DataRequired(), Length(min=2, max=20)])
    email = StringField('信箱',
                            validators =[DataRequired(), Email()])
    picture = FileField('更新個人照片', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('更新')

    # 錯誤訊息
    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('用戶名已經有人使用惹')

    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('信箱已經有人使用惹')

class RequestResetForm(FlaskForm):
    email = StringField('信箱',
                            validators =[DataRequired(), Email()])
    submit = SubmitField('要求更改密碼')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('沒有符合信箱，你必須先註冊會員')

class ResetPasswodForm(FlaskForm):
    password = PasswordField('密碼', validators=[DataRequired()])
    confirm_password = PasswordField('確認密碼',
                            validators =[DataRequired(), EqualTo('password')])
    submit = SubmitField('更改密碼')