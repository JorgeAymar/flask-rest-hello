"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Customers, Characters, Planets, FavCharacters, FavPlanets
from sqlalchemy.orm import exc
from sqlalchemy.exc import IntegrityError
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def people_get_all():
    all_people = Characters.query.all()
    result = []

    for people in all_people:
        result.append(people.serialize())

    return jsonify (result)

@app.route('/people/<int:people_id>', methods=['GET'])
def people_get_id(people_id):
    one_people = Characters.query.get(people_id)

    if one_people == None:
        return jsonify("mensaje: no existe"), 404
    else:
        return jsonify(one_people.serialize())

@app.route('/planet', methods=['GET'])
def planet_get_all():
    all_planet = Planets.query.all()
    result = []

    for planet in all_planet:
        result.append(planet.serialize())

    return jsonify (result)

@app.route('/planet/<int:planet_id>', methods=['GET'])
def planet_get_id(planet_id):
    one_planet = Planets.query.get(planet_id)

    if one_planet == None:
        return jsonify("mensaje: no existe"), 404
    else:
        return jsonify(one_planet.serialize())
    
@app.route('/users', methods=['GET'])
def users_get():
    all_users = Customers.query.all()
    result = []

    for user in all_users:
        result.append(user.serialize())

    return jsonify (result)

#  Listar todos los favoritos que pertenecen al usuario actual.
@app.route('/users/favorites', methods=['GET'])
def favorites_get():
    all_favoritos = Favoritos.query.all()
    result = []

    for favorito in all_favoritos:
        result.append(favorito.serialize())

    return jsonify (result)


@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def planet_post_id(planet_id):
    # Verifica si el planeta existe en la base de datos
    planet = Planets.query.get(planet_id)
    if planet is None:
        return jsonify({"error": "Planet not found"}), 404

    # Obtenemos el customerID desde el request
    data = request.get_json()
    customer_id = data.get("customerID")

    # Verifica si el usuario existe en la base de datos
    customer = Customers.query.get(customer_id)
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    # Crea un nuevo objeto Favoritos
    new_favorite = FavPlanets(customerID=customer_id, planetID=planet_id)

    try:
        # Añade el objeto a la sesión de la base de datos y confirma la transacción
        db.session.add(new_favorite)
        db.session.commit()

        # Retorna una respuesta JSON con la información del favorito creado
        return jsonify(new_favorite.serialize()), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify({"error": "The favorite already exists"}), 409

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def people_post_id(people_id):
    character = Characters.query.get(people_id)
    if character is None:
        return jsonify({"error": "Character not found"}), 404

    data = request.get_json()
    customer_id = data.get("customerID")

    customer = Customers.query.get(customer_id)
    if customer is None:
        return jsonify({"error": "Customer not found"}), 404

    new_favorite = FavCharacters(customerID=customer_id, characterID=people_id)

    try:
        db.session.add(new_favorite)
        db.session.commit()

        return jsonify(new_favorite.serialize()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def planet_del_id(planet_id):
    data = request.get_json()
    customer_id = data.get("customerID")

    favorite = FavPlanets.query.filter_by(customerID=customer_id, planetID=planet_id).first()
    if favorite is None:
        return jsonify({"error": "Favorite not found"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"result": "Favorite deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def people_del_id(people_id):
    data = request.get_json()
    customer_id = data.get("customerID")

    favorite = FavCharacters.query.filter_by(customerID=customer_id, characterID=people_id).first()
    if favorite is None:
        return jsonify({"error": "Favorite not found"}), 404

    try:
        db.session.delete(favorite)
        db.session.commit()

        return jsonify({"result": "Favorite deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
