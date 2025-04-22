from flask import Blueprint, request, jsonify
# Import the token_required decorator to protect routes.
from app.utils.auth import token_required
from app.models import Transaction
from app import db

# Create a Blueprint for transaction-related endpoints.
transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['POST'])
@token_required
def create_transaction(current_user):
    """
    Create a new transaction for the authenticated user.
    
    Expects JSON data with:
      - coin_id: The cryptocurrency identifier.
      - amount: The quantity transacted.
      - price: The price per unit at time of transaction.
      - transaction_type: 'buy' or 'sell'.
    
    Returns:
      JSON response with a success message and HTTP status.
    """
    # Get JSON data from the request.
    data = request.get_json()
    # Create a new Transaction instance with the provided data.
    transaction = Transaction(
        coin_id=data['coin_id'],
        amount=data['amount'],
        price=data['price'],
        transaction_type=data['transaction_type'],
        user_id=current_user.id
    )
    # Add and commit the transaction to the database.
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction created successfully'}), 201