from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Denis'}      # выдуманный пользователь
    return render_template("index.html",
        user=user
    )


@app.route('/module')
def loadModule(module):
    module = module
    return render_template("control.html",
                           module=module)


# функция представления index опущена для краткости

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title='Sign In',
        form=form)
