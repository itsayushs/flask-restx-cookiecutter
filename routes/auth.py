from flask_restx import Resource


class Auth(Resource):
    def get(self, username):
        return {'Hello': username}
