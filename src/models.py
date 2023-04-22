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

    def __repr__(self):
        return '<Characters %r>' % self.name
    
    def serialize(self):
        return {
            "characterID": self.characterID,
            "name": self.name,
            "birthYear": self.birthYear,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender,
            "hairColor": self.hairColor,
            "skinColor": self.skinColor,
            "homeworld": self.homeworld                                                            
        }

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

    def __repr__(self):
        return '<Planets %r>' % self.name
    
    def serialize(self):
        return {
            "planetID": self.planetID,
            "name": self.name,
            "population": self.population,
            "orbitalPeriod": self.orbitalPeriod,
            "diameter": self.diameter,
            "gravity": self.gravity,            
            "terrainGlasslands": self.terrainGlasslands,
            "surfaceWater": self.surfaceWater,
            "climate": self.climate              
        }
    
class FavCharacters(db.Model): 
    __tablename__ = 'favcharacters'
    favoritoID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, ForeignKey('customers.customerID'))
    characterID = db.Column(db.Integer, ForeignKey('characters.characterID'))
    rel_customer = relationship(Customers)
    rel_character = relationship(Characters)

    def __repr__(self):
        return '<FavCharacters %r>' % self.name
    
    def serialize(self):
        return {
            "favoritoID": self.favoritoID,
            "customerID": self.customerID,
            "characterID": self.characterID,
        }

class FavPlanets(db.Model): 
    __tablename__ = 'favplanets'
    favoritoID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, ForeignKey('customers.customerID'))
    planetID = db.Column(db.Integer, ForeignKey('planets.planetID'))
    rel_customer = relationship(Customers)
    rel_planet = relationship(Planets)

    def __repr__(self):
        return '<FavPlanets %r>' % self.name
    
    def serialize(self):
        return {
            "favoritoID": self.favoritoID,
            "customerID": self.customerID,
            "planetID": self.planetID,
        }
    

class Category(db.Model): 
    __tablename__ = 'category'
    categoryID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    rel_planets = relationship(Planets)
    rel_characters = relationship(Characters)

    def __repr__(self):
        return '<Category %r>' % self.name
    
    def serialize(self):
        return {
            "categoryID": self.categoryID,
            "name": self.name
        }
    
    def to_dict(self):
        return {}
 
## Draw from SQLAlchemy base
render_er(db.Model, 'diagram.png')