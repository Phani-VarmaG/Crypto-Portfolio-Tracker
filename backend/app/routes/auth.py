from flask import Blueprint, request, jsonify, current_app  # Import current_app for accessing app config.
from werkzeug.security import generate_password_hash
from app.models import User
from app import db
import jwt
from datetime import datetime, timedelta
# Import the token_required decorator if needed in other routes.
from app.utils.auth import token_required

# Create a Blueprint for authentication-related endpoints.
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    
    Expects JSON data with:
      - username
      - email
      - password
    
    Returns:
      JSON response indicating success.
    """
    data = request.get_json()
    # Hash the user's password before storing it.
    hashed_password = generate_password_hash(data['password'])
    # Create a new User instance.
    user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    # Save the user to the database.
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user.
    
    Expects JSON data with:
      - email
      - password

    Returns:
      JSON response containing an authentication token if credentials are valid.
    """
    # Get credentials from the request.
    auth = request.get_json()
    # Find the user by email.
    user = User.query.filter_by(email=auth['email']).first()

    # Check if user exists and password is correct.
    if not user or not user.check_password(auth['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    # Generate JWT token with an expiration time.
    token = jwt.encode({
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, current_app.config['SECRET_KEY'])

    return jsonify({'token': token})