from flask_restx import Resource, Namespace

api = Namespace('User', description='User Auth JWT')


@api.route('/login')
class userLogin(Resource):
    def get(self):
        return {'Register': 'DummyCode'}
