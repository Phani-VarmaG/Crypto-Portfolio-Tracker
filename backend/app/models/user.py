# filepath: d:\WebDev\crypto-portfolio-tracker\backend\app\models\user.py
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    User model represents a registered user.
    
    Attributes:
      id: Unique identifier for the user.
      username: The user's chosen display name.
      email: The user's email address.
      password_hash: A hashed version of the user's password.
      transactions: A relationship to the user's transactions.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    transactions = db.relationship('Transaction', backref='owner', lazy='dynamic')

    def set_password(self, password):
        """
        Hash and set the user's password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verify the provided password against the stored hash.
        """
        return check_password_hash(self.password_hash, password)