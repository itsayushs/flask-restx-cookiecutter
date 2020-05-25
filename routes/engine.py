from flask_restx import Resource


class Code(Resource):
    def get(self):
        return {'Hello': 'world'}
