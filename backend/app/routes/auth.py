from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.models import User
from app import db
import jwt
from datetime import datetime, timedelta
from app.utils.auth import token_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    user = User.query.filter_by(email=auth['email']).first()
    
    if not user or not user.check_password(auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
        
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, current_app.config['SECRET_KEY'])
    
    return jsonify({'token': token})
