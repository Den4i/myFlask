from app import db
from sqlalchemy.orm import relationship


class User(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    pass_ = db.Column(db.String(50))
    fact_addr_lon = db.Column(db.String(25), nullable=True)
    fact_addr_lat = db.Column(db.String(25), nullable=True)

    __tablename__ = 'users'

    def is_active(self):
        return True

    def get_id(self):
        # returns the user e-mail. not sure who calls this
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        # False as we do not support annonymity
        return False


class Provider(db.Model):
    __tablename__ = 'providers'
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))


class Project(db.Model):
    __tablename__ = 'projects'
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))


class Route(db.Model):
    __tablename__ = 'routs'
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))
    route_active_ = db.Column(db.Integer)


class Object(db.Model):
    __tablename__ = 'objects'
    name_ = db.Column(db.String(20))
    last_rout_ = db.Column(db.Integer, db.ForeignKey('routs.id_'))
    provider_ = db.Column(db.Integer, db.ForeignKey('providers.id_'))

    obj_id_ = db.Column(db.Integer, primary_key=True)
    proj_id_ = db.Column(db.Integer, db.ForeignKey('projects.id_'))

    project = relationship(Project)
    route = relationship(Route)
    provider = relationship(Provider)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, db.Sequence('person_id_seq'), primary_key=True)
    name = db.Column(db.String(50))

    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', backref=db.backref('persons', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Person(id='%s', name='%s')" % (self.id, self.name)


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, db.Sequence('address_id_seq'), primary_key=True)
    email = db.Column(db.String(50))

    def __init__(self, email):
        self.email = email
