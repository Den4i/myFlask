from flask import render_template, flash, redirect, request, url_for, session as ses
from app import app, session
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
        user = session.query(User).filter_by(name_=form.name_.data, pass_=form.pass_.data).first()
        if user:
            ses['user_id'] = user.id_
            flash('Welcome %s' % user.name_)
            return redirect(url_for('index'))
        flash('Неправильный адрес или пароль', 'error-message')
    return render_template("login.html", form=form)


# PROVIDER views
@app.route('/providers/')
def get_providers():
    providers = session.query(Provider)
    return render_template("providers.html", providers=providers)


@app.route('/providers/sortby/id_/')
def get_providers_sortby_id():
    providers = session.query(Provider).order_by(Provider.id_)
    return render_template("providers.html", providers=providers)


@app.route('/providers/sortby/name_/')
def get_providers_sortby_name():
    providers = session.query(Provider).order_by(Provider.name_)
    return render_template("providers.html", providers=providers)


@app.route('/providers/<provider_id_>/')
def get_provider_objects(provider_id_):
    obj = session.query(Object).filter_by(provider_=provider_id_).all()
    return render_template("objects.html", objects=obj)


# PROJECT views
@app.route('/projects/')
def get_projects():
    projects = session.query(Project).all()
    return render_template("projects.html", projects=projects)


@app.route('/projects/sortby/id_/')
def get_projects_sortby_id():
    projects = session.query(Project).order_by(Project.id_)
    return render_template("projects.html", projects=projects)


@app.route('/projects/sortby/name_/')
def get_projects_sortby_name():
    projects = session.query(Project).order_by(Project.name_)
    return render_template("projects.html", projects=projects)


@app.route('/projects/<proj_id>/')
def get_project_objects(proj_id):
    obj = session.query(Object).filter_by(proj_id_=proj_id).all()
    return render_template("objects.html", objects=obj)


# ROUTE
@app.route('/routs/')
def get_routs():
    routs = session.query(Route).all()
    return render_template("routs.html", routs=routs)


@app.route('/routs/sortby/id_/')
def get_routs_sortby_id():
    routs = session.query(Route).order_by(Route.id_)
    return render_template("routs.html", routs=routs)


@app.route('/routs/sortby/name_/')
def get_routs_sortby_name():
    routs = session.query(Route).order_by(Route.name_)
    return render_template("routs.html", routs=routs)


@app.route('/routs/<route_id>/')
def get_routs_objects(route_id):
    obj = session.query(Object).filter_by(last_rout_=route_id).all()
    return render_template("objects.html", objects=obj)


@app.route('/objects/')
def get_objects():
    objects = session.query(Object).all()
    return render_template("objects.html", objects=objects)
