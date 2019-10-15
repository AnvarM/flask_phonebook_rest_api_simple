from settings import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return str({
            'user' : self.username
        })

    def username_password_match(_username, _password):
        user = User.query.filter_by(username = _username).filter_by(password = _password).first()
        if user is None:
            return False
        else:
            return True

    def get_all_users():
        return User.query.all()

    def create_user(_username, _password):
        new_user = User(username =_username, password =_password)
        db.session.add(new_user)
        db.session.commit()