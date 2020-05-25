from flask import Flask
from flask_restx import Api
from routes.routes import init_routes


app = Flask(__name__)
api = Api(app)

init_routes(api)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
