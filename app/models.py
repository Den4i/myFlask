from app import db


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
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))

    __tablename__ = 'providers'


class Project(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.String(50))

    __tablename__ = 'projects'