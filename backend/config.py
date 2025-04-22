import os
from datetime import timedelta

# Configuration class for the Flask backend.
class Config:
    # Secret key used for sessions and JWT encoding.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    # SQLAlchemy Database URI from environment variables.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # JWT token expiration time (in minutes).
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    # Allowed headers for Cross-Origin Resource Sharing (CORS).
    CORS_HEADERS = 'Content-Type'