# Criar as rotas do site
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from fakepinterest.models import User, Photo
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCreateAccount


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        user = User.query.filter_by(email=formlogin.email.data).first()
        if user and bcrypt.check_password_hash(user.password, formlogin.password.data):
            login_user(user)
        return redirect(url_for("perfil", id_user=user.id))
    return render_template("homepage.html", form=formlogin)


@app.route("/criarconta", methods=["GET", "POST"])
def createaccount():
    formcreateaccount = FormCreateAccount()
    if formcreateaccount.validate_on_submit():
        passwordcrypted = bcrypt.generate_password_hash(formcreateaccount.password.data)
        user = User(username=formcreateaccount.username.data,
                    password=passwordcrypted,
                    email=formcreateaccount.email.data)
        database.session.add(user)
        database.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("perfil", id_user=user.id))
    return render_template("createaccount.html", form=formcreateaccount)


@app.route("/perfil/<id_user>")
@login_required
def perfil(id_user):
    if int(id_user) == int(current_user.id):
        #o usuario esta vendo o proprio perfil
        return render_template("perfil.html", user=current_user)
    else:
        user = User.query.get(int(id_user))
        return render_template("perfil.html", user=user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))
