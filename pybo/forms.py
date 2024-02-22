from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.simple import PasswordField, EmailField
from wtforms.validators import DataRequired,EqualTo,Email,Length

#FlaskForm을 상속
class UserLoginForm(FlaskForm):
    email = EmailField('이메일',validators=[DataRequired(),Email()])
    password = PasswordField('비밀번호',validators=[DataRequired()])
class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름',validators=[DataRequired('이름은 입력 필수 입니다.'), Length(min=3,max=25)])

    password1 = PasswordField('비밀번호',validators = [DataRequired(),
                                                   EqualTo('password2','비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인',validators=[DataRequired()])
    email = EmailField('이메일',validators=[DataRequired(),Email()])
class QuestionForm(FlaskForm):
    #글자 수 제한이 있는 경우
    subject = StringField('제목', validators=[DataRequired('제목은 입력 필수')])
    #글자 수 제한이 없는 경우
    contents = TextAreaField('내용', validators=[DataRequired('내용은 입력 필수')])

#답변등록 form
class AnswerForm(FlaskForm):
    contents = TextAreaField('내용', validators=[DataRequired('내용은 필수 입력 항목')])