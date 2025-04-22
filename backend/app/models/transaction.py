# transaction.py
from app import db
from datetime import datetime

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(50), index=True)
    amount = db.Column(db.Float)
    price = db.Column(db.Float)
    transaction_type = db.Column(db.String(10))  # buy/sell
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
