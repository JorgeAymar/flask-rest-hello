import os
from flask_admin import Admin
from models import db, Customers, Characters, Planets, Category, FavCharacters, FavPlanets
from flask_admin.contrib.sqla import ModelView


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Customers, db.session))
    admin.add_view(ModelView(Characters, db.session))
    admin.add_view(ModelView(Planets, db.session))    
    admin.add_view(ModelView(Category, db.session))     
    admin.add_view(ModelView(FavCharacters, db.session))
    admin.add_view(ModelView(FavPlanets, db.session))            
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))