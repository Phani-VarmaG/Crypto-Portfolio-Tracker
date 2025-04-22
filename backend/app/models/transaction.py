from app import db
from datetime import datetime

class Transaction(db.Model):
    """
    Transaction model records a cryptocurrency transaction.
    
    Attributes:
      id: Unique identifier for the transaction.
      coin_id: Identifier of the cryptocurrency.
      amount: Quantity of the coin bought or sold.
      price: Price per unit at time of transaction.
      transaction_type: 'buy' or 'sell'.
      timestamp: Date and time when the transaction occurred.
      user_id: Foreign key linking to the user who made the transaction.
    """
    id = db.Column(db.Integer, primary_key=True)
    coin_id = db.Column(db.String(50), index=True)
    amount = db.Column(db.Float)
    price = db.Column(db.Float)
    transaction_type = db.Column(db.String(10))  # buy/sell
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))