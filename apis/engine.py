from flask_restx import Resource, Namespace

api = Namespace('Engine', description='BusinessLogic')


@api.route('/logic')
class codeLogicGoesHere(Resource):
    def get(self):
        return {'MyCodeLogic': 'DummyCode'}
