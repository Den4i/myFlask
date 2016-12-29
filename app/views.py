from flask import render_template, flash, redirect, request, url_for, session
from app import app
from .forms import LoginForm
from .models import User, Provider


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        user = User.query.filter_by(name_=form.name_.data, pass_=form.pass_.data).first()
        if user:
            session['user_id'] = user.id_
            flash('Welcome %s' % user.name_)
            return redirect(url_for('index'))
        flash('Неправильный адрес или пароль', 'error-message')
    return render_template("login.html", form=form)


@app.route('/providers')
def providers():
    providers = Provider.query.all()
    return render_template("providers.html",
                           providers=providers)
