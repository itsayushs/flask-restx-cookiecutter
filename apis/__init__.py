from flask_restx import Api
from .engine import api as ns1
from .auth import api as ns2

api = Api(
          title='MyNewApi',
          version='6.9',
          description='HelloWorld! This is a New API'
        )

api.add_namespace(ns1, path='/api')
api.add_namespace(ns2, path='/auth')
