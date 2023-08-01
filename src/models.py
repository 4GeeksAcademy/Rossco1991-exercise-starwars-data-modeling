import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(128))
    password = Column(String(250))
    favorites = Column(Integer, ForeignKey('favorites.id'))
    posts = Column(String(4096))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(128))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(20))
    gravity = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    population = Column(Integer)
    residents = Column(Integer, ForeignKey('characters.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(128))
    skin_color = Column(String(128))
    eye_color = Column(String(128))
    birth_year = Column(String(128))
    gender = Column(String(128))
    homeworld = Column(Integer, ForeignKey('planets.id'))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    people = Column(Integer, ForeignKey('characters.id'))
    planets = Column(Integer, ForeignKey('planets.id'))

    # Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
