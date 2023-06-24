from flask import Flask

from .api import get_blueprint as get_api_blueprint

app = Flask(__name__)
app.register_blueprint(get_api_blueprint())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
