from flask_restx import Resource, Namespace, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('Engine', description='BusinessLogic')
parser = reqparse.RequestParser()
parser.add_argument('Authorization', location='headers')


@api.route('/logic')
class codeLogicGoesHere(Resource):
    @api.expect(parser)
    @jwt_required
    def get(self):
        payload = get_jwt_identity()
        username = payload['username']
        password = payload['password']
        role = payload['role']
        print(username, password, role)
        return {'MyCodeLogic': 'DummyCode'}

    def post(self):
        return{'ayush': 'noprotect'}
