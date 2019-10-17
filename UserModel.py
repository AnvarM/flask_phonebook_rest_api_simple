from settings import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return str({
            'user' : self.username
        })

    def username_password_match(_username, _password):
        user = User.query.filter_by(username = _username).first()
        if user is None:
            return False
        else:
            if check_password_hash(user.password, _password):
                return True
            else:
                return False

    def get_all_users():
        return User.query.all()

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def create_user(_username, _password):
        password_hash = generate_password_hash(_password)
        new_user = User(username =_username, password = password_hash)
        db.session.add(new_user)
        db.session.commit()