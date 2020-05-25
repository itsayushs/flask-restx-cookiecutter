from flask import Flask
from flask_jwt_extended import JWTManager
from apis import api

app = Flask(__name__)
JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'ayush-is-daddy'
api.init_app(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
