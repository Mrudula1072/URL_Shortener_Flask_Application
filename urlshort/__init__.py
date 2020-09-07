from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    # print(__name__)
    app.secret_key = 'cgyqagcfyiegcfYE'

    from . import urlshort
    app.register_blueprint(urlshort.bp)
    return app