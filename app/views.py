from flask import render_template, flash, redirect, request, url_for, session
from app import app
from .forms import LoginForm
from .models import User, Provider, Project, Route, Object


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/login/', methods=['GET', 'POST'])
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


@app.route('/providers/')
def get_providers():
    providers = Provider.query.all()
    return render_template("providers.html", providers=providers)


@app.route('/projects/')
def get_projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)


@app.route('/routs/')
def get_routs():
    routs = Route.query.all()
    return render_template("routs.html", routs=routs)


@app.route('/objects/')
def get_objects():
    objects = Object.query.all()
    return render_template("objects.html", objects=objects)


@app.route('/projects/<proj>/')
def get_project_obj(proj):
    obj = Object.query.filter_by(proj_id_=proj).all()
    return render_template("objects.html", objects=obj)
