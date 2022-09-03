import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:////{}".format(
    os.path.join(project_dir, database_filename))

db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    
    # add one demo row which is helping in POSTMAN test
    admin = User(
        username = "abdullyahuza",
        name = "Abdull Yahuza",
        email = "yahuzaabdulrazak@gmail.com",
        password = generate_password_hash("codediam")
    )
    db.session.add(admin)
    db.session.commit()

class User(db.Model):
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    username = Column(String(80))
    name = Column(String(200))
    email = Column(String(120))
    password = Column(String(256))

    def details(self):

        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name
        }

    def __repr__(self):
        return json.dumps(self.details())