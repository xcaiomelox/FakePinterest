from fakepinterest import database, app
from fakepinterest.models import User, Photo

with app.app_context():
    database.create_all()