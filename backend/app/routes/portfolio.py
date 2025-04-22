from flask import Blueprint, jsonify
from app.utils.auth import token_required
from app.utils.coingecko import get_coin_prices
from app.models import Transaction

portfolio_bp = Blueprint('portfolio', __name__)

@portfolio_bp.route('/portfolio', methods=['GET'])
@token_required
def get_portfolio(current_user):
    transactions = Transaction.query.filter_by(user_id=current_user.id).all()
    coin_ids = list({t.coin_id for t in transactions})
    prices = get_coin_prices(coin_ids)
    
    portfolio = []
    for coin_id in coin_ids:
        coin_tx = [t for t in transactions if t.coin_id == coin_id]
        total_amount = sum(t.amount if t.transaction_type == 'buy' else -t.amount for t in coin_tx)
        current_value = total_amount * prices[coin_id]['current_price']
        
        portfolio.append({
            'coin_id': coin_id,
            'amount': total_amount,
            'current_value': current_value,
            'price_data': prices[coin_id]
        })
    
    return jsonify(portfolio)
