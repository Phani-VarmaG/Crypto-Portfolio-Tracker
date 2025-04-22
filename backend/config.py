# backend/config.py
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    CORS_HEADERS = 'Content-Type'
