from flask import Flask
# Import SQLAlchemy for ORM capabilities.
from flask_sqlalchemy import SQLAlchemy
# Import Migrate for handling database migrations.
from flask_migrate import Migrate
# Import CORS to handle cross-origin requests.
from flask_cors import CORS
from config import Config

# Create instances of SQLAlchemy and Migrate.
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    """
    Application factory to create and configure the Flask app.
    
    Args:
      config_class: The configuration class to use.
      
    Returns:
      A fully configured Flask application.
    """
    app = Flask(__name__)
    # Load configurations.
    app.config.from_object(config_class)
    
    # Initialize extensions.
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    # Import Blueprints to register routes.
    from app.routes.auth import auth_bp
    from app.routes.portfolio import portfolio_bp
    from app.routes.transactions import transactions_bp
    
    # Register the Blueprints.
    app.register_blueprint(auth_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(transactions_bp)
    
    return app