from sqlalchemy import Column, String, Integer, Sequence, ForeignKey

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id_ = Column(Integer, primary_key=True)
    name_ = Column(String(50))
    pass_ = Column(String(50))
    fact_addr_lon = Column(String(25), nullable=True)
    fact_addr_lat = Column(String(25), nullable=True)


class Provider(Base):
    __tablename__ = 'providers'
    id_ = Column(Integer, primary_key=True)
    name_ = Column(String(50))


class Project(Base):
    __tablename__ = 'projects'
    id_ = Column(Integer, primary_key=True)
    name_ = Column(String(50))


class Route(Base):
    __tablename__ = 'routs'
    id_ = Column(Integer, primary_key=True)
    name_ = Column(String(50))
    route_active_ = Column(Integer)


class Object(Base):
    __tablename__ = 'objects'
    name_ = Column(String(20))
    last_rout_ = Column(Integer, ForeignKey('routs.id_'))
    provider_ = Column(Integer, ForeignKey('providers.id_'))

    obj_id_ = Column(Integer, primary_key=True)
    proj_id_ = Column(Integer, ForeignKey('projects.id_'))

    project = relationship(Project)
    route = relationship(Route)
    provider = relationship(Provider)


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50))

    address_id = Column(Integer, ForeignKey('address.id'))
    address = relationship('Address', backref=backref('persons', lazy='dynamic'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Person(id='%s', name='%s')" % (self.id, self.name)


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, Sequence('address_id_seq'), primary_key=True)
    email = Column(String(50))

    def __init__(self, email):
        self.email = email
