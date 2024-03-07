#Criar os formulários do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import User
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    button = SubmitField("Fazer login")


class FormCreateAccount(FlaskForm):
    email =StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirm_password = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("password")])
    confirm_button = SubmitField("Criar conta")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("Email já cadastrado! Faça login para continuar")