from flask import Flask 
from app.routes.home_routes import home_bp
app = Flask(__name__)
# Register blueprints
app.register_blueprint(home_bp)