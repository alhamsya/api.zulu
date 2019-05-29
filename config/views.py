from app.main.routes import main_bp
from app.api.routes import api_bp


def register_bp(app):
    # REGISTER BLUEPRINT
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')