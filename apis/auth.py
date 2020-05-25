from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token

api = Namespace('User', description='User Auth JWT')
userpayload = api.model('userdata', {
    'username': fields.String,
    'password': fields.String,
    'role': fields.String,
})


@api.route('/login')
class userLogin(Resource):
    @api.expect(userpayload)
    def post(self):
        # userName = api.payload['username']
        # password = api.payload['password']
        access_token = create_access_token(identity=api.payload)
        return {'JWTToken': access_token}
