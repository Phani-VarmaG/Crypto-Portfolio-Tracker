from flask import Blueprint, jsonify
# Import the token_required decorator to secure the portfolio route.
from app.utils.auth import token_required
# Import the utility function to get coin prices.
from app.utils.coingecko import get_coin_prices
from app.models import Transaction

# Create a Blueprint for portfolio-related endpoints.
portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/portfolio', methods=['GET'])
@token_required
def get_portfolio(current_user):
    """
    Retrieve the user's portfolio by aggregating transactions and applying current coin prices.
    
    Returns:
      JSON response of portfolio details, including coin amounts and current values.
    """
    # Query all transactions for the authenticated user.
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    # Get distinct coin IDs from the transactions.
    coin_ids = list({t.coin_id for t in transactions})
    # Retrieve current coin prices.
    prices = get_coin_prices(coin_ids)
    
    portfolio = []
    # Calculate total amount and current value for each coin.
    for coin_id in coin_ids:
        # Filter transactions for the specific coin.
        coin_tx = [t for t in transactions if t.coin_id == coin_id]
        # Calculate the net amount (buys minus sells).
        total_amount = sum(t.amount if t.transaction_type == 'buy' else -t.amount for t in coin_tx)
        # Calculate the current value based on the latest price.
        current_value = total_amount * prices[coin_id]['current_price']
        
        portfolio.append({
            'coin_id': coin_id,
            'amount': total_amount,
            'current_value': current_value,
            'price_data': prices[coin_id]
        })
    
    return jsonify(portfolio)