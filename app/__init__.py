from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../statics')
    with app.app_context():
        from . import routes
        routes.init_routes(app)
    return app
