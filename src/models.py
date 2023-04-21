from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

db = SQLAlchemy()


class Customers(db.Model):
    __tablename__ = 'customers'
    # Here we define columns for the table.
    customerID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    isActive = db.Column(db.Boolean, unique=False, nullable=True)

    def __repr__(self):
        return '<Customers %r>' % self.name
    
    def serialize(self):
        return {
            "customerID": self.customerID,
            "name": self.name,
            "email": self.email,
            "isActive": self.isActive
        }

class Favoritos(db.Model): 
    __tablename__ = 'favoritos'
    favoritoID = db.Column(db.Integer, primary_key=True)
    customer_ID = db.Column(db.Integer, ForeignKey('customers.customerID'))
    characterID = db.Column(db.Integer, ForeignKey('characters.characterID'))
    planetID = db.Column(db.Integer, ForeignKey('planets.planetID'))
    isActive = db.Column(db.Boolean, unique=False, nullable=True)
    customer = relationship(Customers)

    def __repr__(self):
        return '<Favoitos %r>' % self.name
    
    def serialize(self):
        return {
            "favoritoID": self.favoritosID,
            "customerID": self.name,
            "characterID": self.email,
            "planetID": self.isActive
        }
    
class Characters(db.Model): 
    __tablename__ = 'characters'
    characterID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birthYear = db.Column(db.String(50), unique=False, nullable=True)
    height = db.Column(db.String(50), unique=False, nullable=True)
    mass = db.Column(db.String(50), unique=False, nullable=True)
    gender = db.Column(db.String(50), unique=False, nullable=True)
    hairColor = db.Column(db.String(50), unique=False, nullable=True)
    skinColor = db.Column(db.String(50), unique=False, nullable=True)
    homeworld = db.Column(db.String(50), unique=False, nullable=True)
    categoryID = db.Column(db.Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Planets(db.Model): 
    __tablename__ = 'planets'
    planetID  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    population = db.Column(db.String(50), unique=False, nullable=True)
    rotationPeriod = db.Column(db.String(50), unique=False, nullable=True)
    orbitalPeriod = db.Column(db.String(50), unique=False, nullable=True)
    diameter = db.Column(db.String(50), unique=False, nullable=True)
    gravity = db.Column(db.String(50), unique=False, nullable=True)
    terrainGlasslands = db.Column(db.String(50), unique=False, nullable=True)
    surfaceWater = db.Column(db.String(50), unique=False, nullable=True)
    climate = db.Column(db.String(50), unique=False, nullable=True)
    categoryID = db.Column(db.Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Category(db.Model): 
    __tablename__ = 'category'
    categoryID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    planets = relationship(Planets)
    characters = relationship(Characters)

    def to_dict(self):
        return {}
 
## Draw from SQLAlchemy base
render_er(db.Model, 'diagram.png')