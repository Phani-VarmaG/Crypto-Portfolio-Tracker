from functools import wraps
import jwt
from flask import request, jsonify, current_app
from app.models import User

def token_required(f):
    """
    Decorator that ensures a valid JWT token is present in the request.
    
    If the token is valid, the corresponding user is retrieved and passed to the wrapped function.
    Otherwise, an error response is returned.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # Retrieve the token from the request headers.
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            # Decode the token using the SECRET_KEY from the app's config.
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            # Retrieve the current user from the database.
            current_user = User.query.get(data['user_id'])
        except Exception as e:
            # Token is invalid or expired.
            return jsonify({'message': 'Token is invalid!'}), 401
        # Call the wrapped function with the current user added as first argument.
        return f(current_user, *args, **kwargs)
    return decorated