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


# PROVIDER views
@app.route('/providers/')
def get_providers():
    providers = Provider.query.all()
    return render_template("providers.html", providers=providers)


@app.route('/providers/sortby/id_/')
def get_providers_sortby_id():
    providers = Provider.query.order_by(Provider.id_)
    return render_template("providers.html", providers=providers)


@app.route('/providers/sortby/name_/')
def get_providers_sortby_name():
    providers = Provider.query.order_by(Provider.name_)
    return render_template("providers.html", providers=providers)


@app.route('/providers/<provider_id_>/')
def get_provider_objects(provider_id_):
    obj = Object.query.filter_by(provider_=provider_id_).all()
    return render_template("objects.html", objects=obj)


# PROJECT views
@app.route('/projects/')
def get_projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)


@app.route('/projects/sortby/id_/')
def get_projects_sortby_id():
    projects = Project.query.order_by(Project.id_)
    return render_template("projects.html", projects=projects)


@app.route('/projects/sortby/name_/')
def get_projects_sortby_name():
    projects = Project.query.order_by(Project.name_)
    return render_template("projects.html", projects=projects)


@app.route('/projects/<projId>/')
def get_project_objects(projId):
    obj = Object.query.filter_by(proj_id_=projId).all()
    return render_template("objects.html", objects=obj)


# ROUTE
@app.route('/routs/')
def get_routs():
    routs = Route.query.all()
    return render_template("routs.html", routs=routs)


@app.route('/routs/sortby/id_/')
def get_routs_sortby_id():
    routs = Route.query.order_by(Route.id_)
    return render_template("routs.html", routs=routs)


@app.route('/routs/sortby/name_/')
def get_routs_sortby_name():
    routs = Route.query.order_by(Route.name_)
    return render_template("routs.html", routs=routs)


@app.route('/routs/<routeId>/')
def get_routs_objects(routeId):
    obj = Object.query.filter_by(last_rout_=routeId).all()
    return render_template("objects.html", objects=obj)


@app.route('/objects/')
def get_objects():
    objects = Object.query.all()
    return render_template("objects.html", objects=objects)






