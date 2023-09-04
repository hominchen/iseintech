from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'vnoiejion;laknccowwcaaieknc'

    from .views import views

    # 會成為路徑的前綴開頭
    app.register_blueprint(views, url_prefix='/')

    return app
