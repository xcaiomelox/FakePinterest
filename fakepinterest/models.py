#Criar a estrutura do banco de dados
from fakepinterest import database
from datetime import datetime
class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, unique=True)
    password = database.Column(database.String, nullable=False)
    photo = database.relationship("Photo", backref="user", lazy=True)

class Photo(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    image = database.Column(database.String, default="default.png")
    data_creation = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_user = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
